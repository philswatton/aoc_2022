from argparse import ArgumentParser

# Usage: python 02_rps.py input_file_path
def get_input_file_path() -> str:
    parser = ArgumentParser(description="Calculate total score based on a sequence of Rock Paper Scissors Moves")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    return args.input_file_path

# Function to process a game.
# Rock (A, X) 1, Paper (B, Y) 2, Scissors (C, Z), 3
# Rock beats scissors (1 > 3), paper beats rock (2 > 1), scissors beats paper (3 > 2)
# 0 for loss, 3 for draw, 6 for win
def game_score(result: str):
    if (result[0] == "A" and result[2] == "Z") or (result[0] == "B" and result[2] == "X") or (result[0] == "C" and result[2] == "Y"):
        score = 0
    elif (result[0] == "C" and result[2] == "X") or (result[0] == "A" and result[2] == "Y") or (result[0] == "B" and result[2] == "Z"):
        score = 6
    else:
        score = 3
    if result[2] == "X":
        score += 1
    elif result[2] == "Y":
        score += 2
    else:
        score += 3
    return score

# Main
def main():
    # Get file path
    file_path = get_input_file_path()
    
    # Read in input file
    with open(file_path) as input_file:
        results = input_file.read()
        result_list = results.split("\n")
        score_list = list(map(game_score, result_list))
        print(score_list)

# Run
if __name__ == "__main__":
    main()