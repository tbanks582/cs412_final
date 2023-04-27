def main():
    num_vertices, num_edges = [int(x) for x in input().split()]
    graph = {}
    for i in range(num_vertices):
        graph[i + 1] = set()
    for _ in range(num_edges):
        u, v, w = [int(x) for x in input().split()]
        graph[u].add((v,w))
    longest_path_greedy(graph, 1)


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
    print("Path was: ")

    output = ""
    for i in range(len(longest_path_edges)):
        if i == len(longest_path_edges) - 1:
            output = output + str(longest_path_edges[i])
        else:
            output = output + str(longest_path_edges[i]) + " => "
    print(output)

main()
