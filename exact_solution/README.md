# Exact Solution to Longest Path NP-Complete Problem

This folder has an exhaustive solution to the Longest Path problem that will always be right but runs in exponential time
to demonstrate the exact solution on your own machine:
- clone the repo
- from /cs412_final/,
- run ./run_test_cases.sh in a bash (or zsh with python/python3 alias) terminal

to modify what the value of k is for the connected graph, simply edit the number in connected_input.txt to desired k +1.\
to run on your own graph, replace exact_solution/connected_input.txt or execute:
- python exact_solution/exact_solution.py > output.txt\
to feed custom graph via terminal
