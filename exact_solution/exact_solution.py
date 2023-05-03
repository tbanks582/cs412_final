import time

# main function takes a graph as input and finds the longest path in that graph given v,e,w
def main():
    # print('asd123')
    line = input().split()
    if len(line) == 1:
        return altMain(int(line[0]))
    num_vertices, num_edges = [int(x) for x in line]
    graph = {}
    for i in range(num_vertices):
        graph[i+1] = set()
    for _ in range(num_edges): # feed graph from input
        u, v, w = [int(x) for x in input().split()]
        # might need to add edges going the other way too
        graph[u].add((v,w))
    # for u in graph:
    #     for v in graph.keys():
    #         if u!=v:
    #             graph[u].add((v, 1))
    #             # graph[v].add(u, 1)
    sols = []
    start = time.time_ns()
    cost, path = longest(graph, [], 0, sols)
    end = time.time_ns()
    print('given the graph g: ', graph)
    print('the exact solution is: ', path, ' which has a cost: ', cost)
    print('verification: ', verify(path, cost, graph))

    print('time elapsed: ', (end-start)/1000000000, 's')
    print()
    # verify([0,1,3,2,4,5], 70, graph)
    
    # print(graph)
# alt main creates uniform cost connected graphs of sizes 1-(n-1)
# setting n to 13 causes python to run until my vscode process terminates itself
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
        
        sols = []
        start = time.time_ns()
        cost, path = longest(graph, [], 0, sols)
        end = time.time_ns()
        print('for input size: ', n)
        print('the exact solution is: ', path, ' which has a cost: ', cost)
        print('verification: ', verify(path, cost, graph))
        print('time elapsed: ', (end-start)/1000000000, 's')
        print()



def longest(graph, path,cost, sols):
    maxP = path
    maxC = cost
    for v in graph:
        c, p,  = helper(graph, [v], 0, sols)
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
    # print(total)
    return weight == total
main()
# altMain()
