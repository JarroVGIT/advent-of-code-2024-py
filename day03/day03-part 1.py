# Advent of Code 2024 - Day 03
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
from rich import print
import re

#with open("./day03/example.txt") as f:
with open("./day03/input.txt") as f:
    content = f.read().replace("\n", "")

pattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")

result = 0

for m in re.finditer(pattern, content):
    match = content[m.span()[0]:m.span()[1]]
    left, right = match.split(",")
    left = int(left.replace("mul(", ""))
    right = int(right.replace(")", ""))
    result += left * right

print(result)
