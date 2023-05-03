import random
from math import exp
import time

def main():
    num_vertices, num_edges = [int(x) for x in input().split()]
    graph = {}
    for i in range(num_vertices):
        graph[i + 1] = set()
    for _ in range(num_edges):

        u, v, w = [int(x) for x in input().split()]
        graph[u].add((v,w))

    longest_len = -1
    longest = []
    start = time.time_ns()

    x = 1000
    for i in range(x):
        path = generate_random_path(graph, None, None)
        length = calculate_path_length(graph, path)

        if length > longest_len:
            longest_len = length
            longest = path
        # print("Orignial Path: ", path)
        # print("Original Path Length: ", length)
        if len(path) < 2:
                continue

        annealed_path = annealing_longest_path(graph, 1000, .95, 100, path) 
        annealed_length = calculate_path_length(graph, annealed_path)

        if path != annealed_path:
            if annealed_length > longest_len:
                longest_len = annealed_length
                longest = annealed_path
        
    print("Longest Path: ", longest)
    print("Path Cost: ", longest_len)
    
    end = time.time_ns()
    print('Ran ' + str(x) + ' random paths in '+ str(((end-start) / 1000000000)) + ' Seconds')



def altMain(k):
    for n in range(1, k):
        graph = {}
        for i in range(n):
            graph[i+1] = set()
        for u in graph:
            for v in graph.keys():
                if u!=v:
                    graph[u].add((v, 1))
                    # graph[v].add(u, 1)
        
    longest_len = -1
    longest = []
    start = time.time_ns()

    x = 1000
    for i in range(x):
        path = generate_random_path(graph, None, None)
        length = calculate_path_length(graph, path)

        if length > longest_len:
            longest_len = length
            longest = path
        # print("Orignial Path: ", path)
        # print("Original Path Length: ", length)
        if len(path) < 2:
                continue

        annealed_path = annealing_longest_path(graph, 1000, .95, 100, path) 
        annealed_length = calculate_path_length(graph, annealed_path)

        if path != annealed_path:
            if annealed_length > longest_len:
                longest_len = annealed_length
                longest = annealed_path
        
    print("Longest Path: ", longest)
    print("Path Cost: ", longest_len)
    
    end = time.time_ns()
    print('Ran ' + str(x) + ' random paths in '+ str(((end-start) / 1000000000)) + ' Seconds')


# Returns a random path of random length from the given graph
def generate_random_path(graph, start, old_path):
    marked = set()

    if start == None:
        start = random.choice(list(graph.keys()))

    path = [start]
    marked.add(start)

    if len(graph[start]) == 0:
            return path 
    next_node = random.choice(tuple(graph[start]))[0]
    path.append(next_node)
    marked.add(next_node)

    available = {edge[0] for edge in graph[next_node]}

    if old_path != None:
        for vert in available.copy():
            if vert in old_path:
                available.remove(vert)

    while next_node is not None:
        
        if len(available) == 0:
            return path 
        
        random_neighbor = random.choice(tuple(available))

        if random_neighbor not in marked:
            next_node = random_neighbor
            path.append(next_node)
            marked.add(next_node)
            available = {edge[0] for edge in graph[next_node]}
        else:
            available.remove(random_neighbor)
            
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


def random_vertex_path(graph, path):

    available = path[1:]
    new_path = path.copy()

    # vertex before the one that will be switched. Switch will occur with on of this vertex's neighbors
    vertex = random.choice(available)

    while len(graph[vertex]) == 0:
        available.remove(vertex)

        if len(available) == 0:
            return new_path
        vertex = random.choice(available)

    # index of the vertex that will be swapped with previous's neighbor
    swap_index = path.index(vertex) + 1

    # if vertex is last in path
    if vertex == path[-1]:
        neighbor = random.choice(tuple(graph[path[path.index(vertex) - 1]]))
        new_path[-1] = neighbor[0]
        return new_path
    

    # if vertex chosen is second to last in path
    if vertex == path[-2]:
        neighbor = random.choice(tuple(graph[path[path.index(vertex)]]))
        new_path[swap_index] = neighbor[0]
        return new_path

    new_path = generate_random_path(graph, vertex, path)
    
    return new_path



def annealing_longest_path(graph, inital_temp, cool_rate, stop_temp, path):

    current_length = calculate_path_length(graph, path)

    best_path = path
    best_length  = current_length


    temp = inital_temp

    while temp > stop_temp:
        new_path = random_vertex_path(graph, path)
        
        new_length = calculate_path_length(graph, new_path)


        if new_length > current_length:
            
            path = new_path
            current_length = new_length

            if new_length > best_length:
                
                best_path = new_path
                best_length = new_length
        
        else:
            accept_probability = exp((new_length - current_length) / temp)

            if random.random() < accept_probability:
                current_length = new_length
                path = new_path

        temp = temp * cool_rate

    return best_path


main()
