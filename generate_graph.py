import random

def generate_complete_directed_graph(num_vertices, min_weight, max_weight, output_file):
    with open(output_file, 'w') as f:
        for i in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                if i != j:
                    weight = random.randint(min_weight, max_weight)
                    f.write(f'{i} {j} {weight}\n')

if __name__ == "__main__":
    num_vertices = int(input())  # Number of vertices in the graph
    min_weight = 1    # Minimum edge weight
    max_weight = 20   # Maximum edge weight
    output_file = 'input.txt'
    
    generate_complete_directed_graph(num_vertices, min_weight, max_weight, output_file)
