def main():
    # print('asd123')
    num_vertices, num_edges = [int(x) for x in input().split()]
    graph = {}
    for i in range(num_vertices):
        graph[i] = set()
    for _ in range(num_edges):
        u, v, w = [int(x) for x in input().split()]
        # might need to add edges going the other way too
        graph[u].add((v,w))
    sols = []
    cost, path = longest(graph, [], 0, sols)
    print(cost, path)
    verify(path, cost, graph)
    # verify([0,1,3,2,4,5], 70, graph)
    
    print(graph)


def longest(graph, path,cost, sols):
    maxP = path
    maxC = cost
    for v in graph:
        c, p = helper(graph, [v], 0, sols)
        # print(v, c,p)
        if c > maxC:
            maxC = c
            maxP = p
    maxC, maxP = max(sols)
    return maxC, maxP
    
def helper(graph, path, cost, sols):
    newCost = cost
    newPath = path
    for adj, weight in graph[path[-1]]:
        newCost = cost
        newPath = path
        # print(path, adj)
        if adj not in path:
            c, p = helper(graph, path + [adj], cost+weight, sols)
            if c>newCost:
                newCost = c
                newPath = p
    # print(newCost, newPath)
    sols.append((newCost, newPath))
    return newCost, newPath

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
