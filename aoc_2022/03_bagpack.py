from argparse import ArgumentParser

# Usage: python 03_bagpack.py input_file_path
def get_input_file_path() -> str:
    parser = ArgumentParser(description="AOC Day 3 Function")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    return args.input_file_path

# Part 1: function that finds common letter in compartments
def find_common_letter_1(bag: str) -> str:
    num_contents = len(bag)
    half = int(num_contents/2) # can assume all inputs are even
    compartment_1 = set(bag[0:half])
    compartment_2 = set(bag[half:num_contents])
    return (compartment_1 & compartment_2).pop()

# Part 2: function that finds common letter across 3 strings
def find_common_letter_2(bag_1: str, bag_2: str, bag_3: str) -> str:
    return (set(bag_1) & set(bag_2) & set(bag_3)).pop()

# Function that converts letters to priority numbers a-z: 1-26; A-Z: 27-52
def letter_to_priority(letter: str) -> int:
    num = ord(letter)
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
        
        # Part 1: Calculate sum of priorities
        priority_list = list(map(lambda input: letter_to_priority(find_common_letter_1(input)), items_list))
        print("Sum of item priorities: " + str(sum(priority_list)))
        
        # Part 2: Calculate sum of badges
        badge_list = list(map(lambda i: letter_to_priority(find_common_letter_2(items_list[i], items_list[i+1], items_list[i+2])), range(0, len(items_list), 3)))
        print("Sum of badges: " + str(sum(badge_list)))
        
# Run
if __name__ == "__main__":
    main()