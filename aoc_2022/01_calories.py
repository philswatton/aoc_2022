import re

# Iterate over input file, calculate list of elf total calories
elfList = [0]
iterator = 0
with open("aoc_2022/01_list.txt") as inputFile:
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
        