from argparse import ArgumentParser

# Usage: python 08_trees.py input_file_path
def get_input_file_path() -> str:
    parser = ArgumentParser(description="AOC Day 0 Function")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    return args.input_file_path

# Row search function
def row_search(grid: list[str], nrow: int, col_start: int, col_fin: int, increment: int) -> set:
    out = set()
    for i in range(1, nrow-1):
        prev_height = grid[i][col_start-increment]
        for j in range(col_start, col_fin, increment):
            if grid[i][j] > prev_height:
                out.add((i,j))
                prev_height = grid[i][j]
    return out

# Column search function
def col_search(grid: list[str], ncol: int, row_start: int, row_fin: int, increment: int) -> set:
    out = set()
    for j in range(1, ncol-1):
        prev_height = grid[row_start-increment][j]
        for i in range(row_start, row_fin, increment):
            if grid[i][j] > prev_height:
                out.add((i,j))
                prev_height = grid[i][j]
    return out

# Function that can search for visible trees
def tree_search(grid: list[str]) -> set[int]:
    # Dimensions
    nrow = len(grid)
    ncol = len(grid[0])
    
    # search in all directions, indexing trees that are visible
    left_visible = row_search(grid, nrow, 1, ncol-2, 1)
    right_visible = row_search(grid, nrow, ncol-2, 0, -1)
    top_visible = col_search(grid, ncol, 1, nrow-2, 1)
    bottom_visible = col_search(grid, ncol, nrow-2, 0, -1)
    
    # Union
    visible_union = right_visible | left_visible | top_visible | bottom_visible
    
    # Number visible
    n_visible = len(visible_union) + (nrow-1)*2 + (ncol-1)*2
    
    # Return
    return n_visible

# Main
def main():
    # Get file path
    file_path = get_input_file_path()
    
    # Read in input file
    with open(file_path) as input_file:
        tree_grid = input_file.read().rstrip().split("\n")
    
    # Part 1: Number of visible trees
    n_visible = tree_search(tree_grid)
    print("Number of trees visible: " + str(n_visible))
    
    

# Run
if __name__ == "__main__":
    main()