import time

def main():
    
    num_vertices = int(input())
    graph = {}
    for i in range(num_vertices):
        graph[i + 1] = set()
    for i in range(90):

        u, v, w = [int(x) for x in input().split()]
        graph[u].add((v,w))
    sols = []
    start = time.time_ns()
    cost, path = longest(graph, [], 0, sols)
    print("Path: ", path)
    verify(path, cost, graph)
    end = time.time_ns()
    print('Ran in '+ str((end-start) / 1000000000) + ' Seconds')
    # verify([0,1,3,2,4,5], 70, graph)
    
    # print(graph)


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
    print("Total: ", total)
main()
