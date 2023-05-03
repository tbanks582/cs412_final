# cs412_final
# author: Trevor Nicholas, Kiavash Seraj
final project for Applied Algorithms

longest path NP-Complete problem


input/output format:

The first line is the total flow of the network. Then, each edge that is part of the min cut is printed on a separate line. 
First line of the output has the cost of the longest path, and the second line prints the path itself.

sample input:
6 9 \
1 2 20\
1 3 10\
2 3 10\
2 4 5\
4 3 15\
3 5 10\
5 4 10\
4 6 15\
5 6 20\

sample output (exact solution):
given the graph g:  {1: {(2, 20), (3, 10)}, 2: {(4, 5), (3, 10)}, 3: {(5, 10)}, 4: {(3, 15), (6, 15)}, 5: {(4, 10), (6, 20)}, 6: set()}\
the exact solution is:  [1, 2, 4, 3, 5, 6]  which has a cost:  70\
verification:  True\
time elapsed:  0.0 s\


