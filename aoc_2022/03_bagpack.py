from argparse import ArgumentParser

# Usage: python 03_bagpack.py input_file_path
def get_input_file_path() -> str:
    parser = ArgumentParser(description="AOC Day 3 Function")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    return args.input_file_path

# Function that finds common letter in compartments
def find_common_letter(contents: str) -> str:
    num_contents = len(contents)
    half = int(num_contents/2) # can assume all inputs are even
    compartment_1 = set(contents[0:half])
    compartment_2 = set(contents[half:num_contents])
    return compartment_1 & compartment_2

# Function that converts letters to priority numbers a-z: 1-26; A-Z: 27-52
def contents_to_priority(contents: str) -> int:
    letter = find_common_letter(contents)
    num = ord(letter.pop())
    if num >= 97:
        return num - 96
    else:
        return num - 38

# Main
def main():
    # Get file path
    file_path = get_input_file_path()
    
    # Read in input file
    with open(file_path) as input_file:
        # Process input
        items = input_file.read().rstrip()
        items_list = items.split("\n")
        
        # Calculate sum of priorities
        priority_list = list(map(contents_to_priority, items_list))
        print("Sum of item priorities: " + str(sum(priority_list)))

# Run
if __name__ == "__main__":
    main()