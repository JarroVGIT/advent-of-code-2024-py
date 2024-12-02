# Advent of Code 2024 - Day 02
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
from rich import print
#import re

#with open("./day02/example.txt") as f:
with open("./day02/input.txt") as f:
    content = f.read().split("\n")

reports = []
for line in content:
    report = list(map(int, line.split()))
    reports.append(report)

result = 0
for report in reports:
    if report[0] > report[1] and 1 <= report[0]-report[1] <= 3:
        inc = False
    elif report[0] < report[1] and 1 <= report[1]-report[0] <= 3:
        inc = True
    else:
        continue
    
    current_result = True
    for idx, r in enumerate(report):
        if idx == 0:
            continue
        if (inc and 1 <= r-report[idx-1] <= 3) or (not inc and 1 <= report[idx-1]-r <= 3):
            continue
        else:
            current_result = False
            break
    if current_result:
        print(report)
        result += 1

print(result)
