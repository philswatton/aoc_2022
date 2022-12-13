from argparse import ArgumentParser
from typing import Optional
DIR, FILE = "dir", "file"

# Usage: python 07_file.py input_file_path
def get_input_file_path() -> str:
    parser = ArgumentParser(description="AOC Day 0 Function")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    return args.input_file_path

# Define a class that keeps track of parent and children
class Node:
    def __init__(self,
                 type: str,
                 children: Optional[dict] = None,
                 parent: Optional["Node"] = None,
                 size: Optional[int] = None
                ) -> None:
        self.type = type
        self.parent = parent
        self.children = children
        self.size = size

# Function to parse terminal output into Nodes
def output2filesystem(terminal_output: list[str]) -> dict:
    filesystem = Node(DIR, {}, None)
    current = filesystem
    for line in terminal_output:
        if line[0:4] == "$ cd":
            if line[5] == "/":
                current = filesystem
            elif line[5:] == "..":
                current = current.parent
            else:
                current = current.children[line[5:]]
        elif line[0:3] == "dir":
            current.children[line[4:]] = Node(DIR,
                                              children={},
                                              parent=current)
        elif line[0:4] != "$ ls":
            parts = line.split()
            current.children[parts[1]] = Node(FILE,
                                              children=None,
                                              parent=current,
                                              size=int(parts[0]))
    return filesystem
        
# Function that walks over Node structure, returns list of file sizes
    

# Main
def main():
    # Get file path
    file_path = get_input_file_path()
    
    # Read in input file
    with open(file_path) as input_file:
        terminal_output = input_file.read().rstrip().split("\n")
    
    # Parse output into file system
    filesystem = output2filesystem(terminal_output)
    print(filesystem.children)
    print(filesystem.children["d"].children)

# Run
if __name__ == "__main__":
    main()