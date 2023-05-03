# cs412_final
# author: Trevor Nicholas, Kiavash Seraj
Final project for Applied Algorithms (cs412)

# Longest Path NP-Complete problem project


## Input/Output Format:

The first line of input is the number of vertexes, then the number of edges to add. The rest of the input encodes edges as u,v,w.\
The first line of the output prints the graph, second prints the solution and cost, third prints the result of verification, fourth prints wall clock time using python's time.time_ns().

sample input:\
6 9 \
1 2 20\
1 3 10\
2 3 10\
2 4 5\
4 3 15\
3 5 10\
5 4 10\
4 6 15\
5 6 20

sample output (exact solution):\
given the graph g:  {1: {(2, 20), (3, 10)}, 2: {(4, 5), (3, 10)}, 3: {(5, 10)}, 4: {(3, 15), (6, 15)}, 5: {(4, 10), (6, 20)}, 6: set()}\
the exact solution is:  [1, 2, 4, 3, 5, 6]  which has a cost:  70\
verification:  True\
time elapsed:  0.0 s

## Instructions

- Instructions for usage of the exact solution can be found in exact_solution/README.md
- Approximation algorithm follows the same input scheme as the exact solution and can write to a file.
- Presentation .pptx can be found in /presentation
