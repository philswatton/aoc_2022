from argparse import ArgumentParser

# Usage: python 00_template.py input_file_path
def get_input_file_path() -> str:
    parser = ArgumentParser(description="AOC Day 0 Function")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    return args.input_file_path

# Main
def main():
    # Get file path
    file_path = get_input_file_path()
    
    # Read in input file
    with open(file_path) as input_file:
        print("Hello, world")

# Run
if __name__ == "__main__":
    main()