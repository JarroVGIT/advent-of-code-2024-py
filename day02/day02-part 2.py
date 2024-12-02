# Advent of Code 2024 - Day 02
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
from copy import copy
#import re

#with open("./day02/example.txt") as f:
with open("./day02/input.txt") as f:
    content = f.read().split("\n")

def check_safety(report: list[int], increase: bool, retry_allowed:bool) -> bool:
    # Check safety, if not safe, check with new reports but with retry is false
    current_result = True
    retry_used = False
    for idx, r in enumerate(report):
        if idx == 0:
            continue
        if (increase and 1 <= r-report[idx-1] <= 3) or \
            (not increase and 1 <= report[idx-1]-r <= 3):
            continue
        elif retry_allowed and not retry_used:
            r1 = report[0:idx] + report[idx+1:] # retry without current idx
            r2 = report[0:idx-1] + report[idx:] # retry without previous idx
            if check_safety(r1, increase, False) or check_safety(r2, increase, False):
                continue
            else:
                current_result = False
                break
        else:
            current_result = False
            break
    return current_result

reports = []
for line in content:
    report = list(map(int, line.split()))
    reports.append(report)

result = 0
for report in reports:
    increases = 0
    samesies = 0
    decreases = 0
    for idx, r in enumerate(report):
        if idx == 3:
            break
        if r > report[idx+1]:
            decreases += 1
        elif r < report[idx+1]:
            increases += 1
        else:
            samesies += 1

    if increases >= 2:
        inc = True
    elif decreases >= 2:
        inc = False
    else:
        continue
    

    if check_safety(report, inc, True):
        result += 1

print(result)