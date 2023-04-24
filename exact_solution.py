def main():
    print('asd123')
    num_vertices, num_edges = [int(x) for x in input().split()]
    graph = {}
    for i in range(num_vertices):
        graph[i] = set()
    for _ in range(num_edges):
        u, v, w = [int(x) for x in input().split()]
        graph[u].add((v,w))
    verify([0,1,3,2,4,5], 70, graph)
    print(graph)



def verify(path, weight, graph):
    total = 0
    start = path[0]
    u = -1
    
    for v in path:
        if v == start:
            u = start
        else:
            for e, w in graph[u]:
                if e == v:
                    total += w
            u = v
    print(total)
    print(weight == total)
main()