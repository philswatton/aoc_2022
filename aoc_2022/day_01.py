import re

elfList = [0]
elfIndex = 0
with open("aoc_2022/01_list.txt") as inputFile:
    for line in inputFile.readlines():
        lineRegex = re.search("^\d+", line)
        if lineRegex == None:
            elfIndex += 1
            elfList.append(0)
        else:
            elfList[elfIndex] = elfList[elfIndex] + float(lineRegex.group(0))
            
print(elfIndex)
print(elfList)
        