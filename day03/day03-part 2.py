# Advent of Code 2024 - Day 03
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
import re

#with open("./day03/example.txt") as f:
#with open("./day03/example-2.txt") as f:
with open("./day03/input.txt") as f:
    content = f.read().replace("\n", "")

pattern = r"(?:mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))"

do = True
result = 0
for m in re.findall(pattern, content):
    if m == "do()":
        do = True
    elif m == "don't()":
        do = False
    elif do:
        left, right = m.split(",")
        left = int(left.replace("mul(", ""))
        right = int(right.replace(")", ""))
        result += left * right
    else:
        continue

print(result)


