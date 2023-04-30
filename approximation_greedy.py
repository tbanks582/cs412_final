import random
from math import exp

def main():
    num_vertices, num_edges = [int(x) for x in input().split()]
    graph = {}
    for i in range(num_vertices):
        graph[i + 1] = set()
    for _ in range(num_edges):
        u, v, w = [int(x) for x in input().split()]
        graph[u].add((v,w))

    # random_key = random.choice(list(graph.keys()))
    # print(random_key)
    # longest_path_greedy(graph, random_key)
    # print("Graph: ", graph)
    for _ in range(100):
        path = generate_random_path(graph)
        
        if len(path) < 2:
            continue
        annealed_path = annealing_longest_path(graph, 1000, .9, 100, path)
        print("Orignial Path: ", path)
        if path != annealed_path:
            print("Better path found: ",annealed_path)
        print("\n")
        


# Returns a random path of random length from the given graph
def generate_random_path(graph):
    marked = set()
    
    start = random.choice(list(graph.keys()))

    path = [start]
    marked.add(start)

    if len(graph[start]) == 0:
            return path 
    next_node = random.choice(tuple(graph[start]))[0]
    marked.add(next_node)

    while next_node is not None:
        path.append(next_node)
        if len(graph[next_node]) == 0:
            return path 
        random_neighbor = random.choice(tuple(graph[next_node]))[0]
        if random_neighbor not in marked:
            next_node = random_neighbor
    return path

# Returns the cumulative weight of the path given
def calculate_path_length(graph, path):
    path_length = 0
    for i in range(len(path) - 1):
        current_vertex = path[i]
        next_vertex = path[i + 1]
        edge_weight = None

        for neighbor, weight in graph[current_vertex]:
            if neighbor == next_vertex:
                edge_weight = weight
                break

        if edge_weight is None:
            # The path is not valid; it contains an edge that does not exist in the graph.
            return float('-inf')
        else:
            path_length += edge_weight

    return path_length

# checks if an edge exitsts between two verticies
def edge_exists(graph, u, v):
    return any(neighbor == v for neighbor, _ in graph[u])

def random_swap_verticies(graph, path):
    available = path.copy()
    new_path = path.copy()

    # vertex before the one that will be switched. Switch will occur with on of this vertex's neighbors
    vertex = random.choice(path)

    while len(graph[vertex]) == 0:
        available.remove(vertex)

        vertex = random.choice(available)

    # index of the vertex that will be swapped with previous's neighbor
    swap_index = path.index(vertex) + 1

    # if vertex is last in path
    if vertex == path[-1]:
        neighbor = random.choice(tuple(graph[path[path.index(vertex) - 1]]))
        new_path[-1] = neighbor
        return new_path
    # if vertex chosen is second to last in path
    if vertex == path[-2]:
        neighbor = random.choice(tuple(graph[path[path.index(vertex)]]))
        new_path[swap_index] = neighbor
        return new_path


    for neighbor in graph[vertex]:
        neighbor_vertex = neighbor[0]

        if edge_exists(graph, neighbor_vertex, path[swap_index + 1]):
            new_path[swap_index] = neighbor_vertex
            
            return new_path



def annealing_longest_path(graph, inital_temp, cool_rate, stop_temp, path):

    current_length = calculate_path_length(graph, path)

    best_path = path
    best_length  = current_length


    temp = inital_temp

    while temp > stop_temp:
        new_path = random_swap_verticies(graph, path)
        new_length = calculate_path_length(graph, new_path)

        if new_length > current_length:
            path = new_path
            current_length = new_length

            if new_length > best_length:
                print("success")
                best_path = new_path
                best_length = new_length
        
        else:
            accept_probability = exp((new_length - current_length) / temp)

            if random.random() < accept_probability:
                current_length = new_length
                path = new_path

        temp = temp * cool_rate

    return best_path






















# Find the longest path by taking the a verticies heaviest edge rinse and repreat
def longest_path_greedy(graph, start):
    marked = set()
    curr = start

    longest_path_edges = [curr]
    path_length = 0

    while curr is not None:
        marked.add(curr)
        next = None
        longest_path = float("-inf")

        # check all neighbors and grab the longest one (greedy)
        for neighbor, weight in graph[curr]:
            if neighbor not in marked and weight > longest_path:
                next = neighbor
                longest_path = weight

        if next is not None:
            longest_path_edges.append(next)
            path_length = path_length + longest_path
        curr = next
    
    print("Length of the longest path is approximately ", path_length)

    output = "Path was: "
    for i in range(len(longest_path_edges)):
        if i == len(longest_path_edges) - 1:
            output = output + str(longest_path_edges[i])
        else:
            output = output + str(longest_path_edges[i]) + " => "
    print(output)

main()
