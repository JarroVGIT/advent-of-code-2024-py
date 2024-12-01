# Advent of Code 2024 - Day 01
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
#import re

#with open("./day01/2-example.txt") as f:
with open("./day01/input.txt") as f:
    content = f.read().split("\n")

left = []
right = []
for line in content:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

result = 0
for i in left:
    result += i * right.count(i)

print(result)