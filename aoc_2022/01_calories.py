from argparse import ArgumentParser
import re

# Usage: python 01_calories.py input_file_path
def process():
    parser = ArgumentParser(description="Calculate elf with the most calories")
    parser.add_argument("input_file_path") # required (positional) arguments
    args = parser.parse_args()
    print(args)
    return args

# Main
def main():
    # Get file path
    file_path = process().input_file_path
    
    # Iterate over input file, calculate list of elf total calories
    elfList = [0]
    iterator = 0
    with open(file_path) as inputFile:
        for line in inputFile.readlines():
            lineRegex = re.search("^\d+", line)
            if lineRegex == None:
                iterator += 1 #assuming only one new line between elves
                elfList.append(0)
            else:
                elfList[iterator] = elfList[iterator] + float(lineRegex.group(0))

    # Get index of highest calorie elf
    elfIndex = elfList.index(max(elfList))

    # Print output to console
    print("Elf " + str(elfIndex+1) + " is carrying the most calories")

# Run
if __name__ == "__main__":
    main()