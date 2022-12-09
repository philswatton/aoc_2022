from argparse import ArgumentParser
import math

# Usage: python 05_crates.py input_file_path
def get_input_file_path() -> str:
    parser = ArgumentParser(description="AOC Day 5 Function")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    return args.input_file_path

# Function to compute series 1, 5, 9, ...
def compute_series(num: int) -> list[int]:
    out = []
    current = -3
    for i in range(num):
        current += 4
        out.append(current)
    return out

# Input boxes to array of boxes
def box2array(boxes: list[str]) -> list[str]:
    num_slots = math.ceil(len(boxes[0])/4)
    content_indices = compute_series(num_slots)
    box_array = [[] for _ in range(num_slots)]
    for line in boxes:
        for i in range(num_slots):
            if line[content_indices[i]] != " ":
                box_array[i].append(line[content_indices[i]])
    return box_array

# Take one instruction and apply it
def apply_instruction(boxarr: list[str], instruction: str) -> list[str]:
    instruction = instruction.split()
    num_moves = int(instruction[1])
    move_from = int(instruction[3])
    move_to = int(instruction[5])
    for i in range(num_moves):
        boxarr[move_to-1].insert(0, boxarr[move_from-1].pop(0))
    return(boxarr)

# Parse the whole set of instructions
def parse_instructions(boxarr: list[str], instructions: list[str]) -> list[str]:
    for instruction in instructions:
        boxarr = apply_instruction(boxarr, instruction)
    return boxarr

# Function to print all top boxes
def print_top_box(boxarr: list[str]) -> str:
    out = ""
    for i in range(len(boxarr)):
        out += boxarr[i][0]
    return out

# Main
def main():
    # Get file path
    file_path = get_input_file_path()
    
    # Read in input file
    with open(file_path) as input_file:
        file = input_file.read().rstrip().split("\n")
        
        # Get point where boxes stop and instructions start
        index = [i for i in range(len(file)) if file[i] == ""][0]
        
        # Separate out relevant lines
        boxes = file[0:(index-1)]
        locations = file[index-1]
        instructions = file[(index+1):len(file)]
        
        # Array of boxes
        box_arr = box2array(boxes)
        
        # Part 1: parse instructions, get value of top boxes
        out1 = parse_instructions(box_arr, instructions)
        print("The top boxes contain the letters " + str(print_top_box(out1)))

# Run
if __name__ == "__main__":
    main()