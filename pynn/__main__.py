import os
import sys
import itertools
from .nearest_neighbor_index import NearestNeighborIndex

def main():
    # Check command line arguments
    if len(sys.argv) < 3:
        print("Error: No input file provided")
        return
    elif len(sys.argv) <= 4:
        index_file = read_txt_file(sys.argv[1])
        if index_file is None:
            return
        query_file = read_txt_file(sys.argv[2])
        if query_file is None:
            return
    else:
        print("Error: Too many arguments")
        return

    if len(sys.argv) == 4:
        data = call_nni(index_file, query_file)
        output_file = sys.argv[3]
        out_file(query_file, data, output_file)
    else:
        print(call_nni(index_file, query_file))

def call_nni(index_file, query_file):
    #call NNI
    uut = NearestNeighborIndex(index_file)
    output = []
    for point in query_file:
        output.append(uut.find_nearest(point))
    
    return output
        
def read_txt_file(file):
    try:
        with open(file, "r") as f:
            lines = f.readlines()

        points = []
        for line in lines:
            try:
                # Parse tuple of floats from line
                point = tuple(float(num) for num in line.replace('\n', '').split(' '))
                points.append(point)
            except ValueError:
                # Skip lines that can't be parsed as tuples of floats
                print(f"Warning: Skipping invalid line in {file}: {line}")
        return points
    except FileNotFoundError:
        print(f"Error: File not found: {file}")
    except IOError:
        print(f"Error: Could not read file: {file}")

def out_file(input_list, output_list, output_file):
    if len(input_list) != len(output_list):
        print("Error: input and output sizes do not correspond")
        return

    with open(output_file, "w") as f:
        for query, ans in zip(input_list, output_list):
            f.write(f"{query} -> {ans}\n")

if __name__ == "__main__":
    main()