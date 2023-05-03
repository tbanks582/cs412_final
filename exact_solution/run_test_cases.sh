#! /usr/bin/bash
python exact_solution/exact_solution.py < exact_solution/sample_inputs/connected_random_input.txt > exact_solution/outputs/connected_random_output.txt
python exact_solution/exact_solution.py < exact_solution/sample_inputs/sparse_uniform_input.txt > exact_solution/outputs/sparse_uniform_output.txt
python exact_solution/exact_solution.py < exact_solution/sample_inputs/connected_uniform_input.txt > exact_solution/outputs/connected_uiform_output.txt
