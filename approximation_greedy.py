import random

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
    print(graph)
    generate_random_path(graph)


def generate_random_path(graph):
    marked = set()
    start = random.choice(list(graph.keys()))

    path = [start]
    marked.add(start)

    next_node = random.choice(list(graph[start]))
    marked.add(next_node)

    while next_node is not None:
        path.append(next_node)
        random_neighbor = random.choice(list(graph[start]))
        if random_neighbor not in marked:
            next_node = random_neighbor
    return path



# def annealing_longest_path(graph, inital_temp, cool_rate, stop_temp, path):



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
