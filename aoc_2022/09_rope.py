from argparse import ArgumentParser
from typing import Union

# Usage: python 09_rope.py input_file_path
def get_input_file_path() -> str:
    parser = ArgumentParser(description="AOC Day 0 Function")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    return args.input_file_path

# Sign function
def sign(num: Union[int, float]) -> int:
    if num > 0:
        return 1
    if num < 0:
        return -1
    if num == 0:
        return 0

# Function to compute a single move
def update_positions(direction: str, num_moves: int, head_pos: list[int], tail_pos: list[int]):
    
    # Sign of head movement direction
    if direction == "R" or direction == "U":
        move_sign = 1
    else:
        move_sign = -1
    
    # Index of head movement direction
    if direction == "L" or direction == "R":
        index = 0
    else:
        index = 1
    
    # Track unique positions of tail
    tail_visited = []
    
    # Loop over, update tail if necessary
    for i in range(num_moves):
        # Move head
        head_pos[index] += move_sign
        
        # Get differences
        row_difference = head_pos[0] - tail_pos[0]
        col_difference = head_pos[1] - tail_pos[1]
        
        # Move tail left or right
        if abs(row_difference) > 1 and col_difference == 0:
            tail_pos[index] += move_sign
        
        # Move tail up or down
        if row_difference == 0 and abs(col_difference) > 1:
            tail_pos[index] += move_sign
        
        # Move tail diagnoally
        if (abs(row_difference) > 1 and abs(col_difference) > 0) or (abs(row_difference) > 0 and abs(col_difference) > 1):
            tail_pos[0] += sign(row_difference)
            tail_pos[1] += sign(col_difference)
        
        # Store new tail position
        tail_visited.append(tuple(tail_pos))
    
    # Return
    return head_pos, tail_pos, tail_visited

# Function that iterates through moves and stores positions
def compute_positions(move_list: list[str]):
    # Initialise tracking vars
    head_pos = [0,0]
    tail_pos = [0,0]
    tail_visited = [(0,0)]
    
    # Iterate over moves
    for move in move_list:
        direction, number = move.split()
        head_pos, tail_pos, new_tail_visited = update_positions(direction, int(number), head_pos, tail_pos)
        tail_visited = tail_visited + new_tail_visited
    
    # Return
    return set(tail_visited)

# Main
def main():
    # Get file path
    file_path = get_input_file_path()
    
    # Read in input file
    with open(file_path) as input_file:
        motions = input_file.read().rstrip().split("\n")
    
    # Part 1: Compute number of positions visited by tail
    tail_vistied = compute_positions(motions)
    print("The tail has visited " + str(len(tail_vistied)) + " unique positions")

# Run
if __name__ == "__main__":
    main()