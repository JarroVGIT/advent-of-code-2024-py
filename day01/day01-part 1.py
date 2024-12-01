# Advent of Code 2024 - Day 01
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
from rich import print
#import re

#with open("./day01/1-example.txt") as f:
with open("./day01/1-input.txt") as f:
    content = f.read().split("\n")

left = []
right = []
for line in content:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

sum_of_distances = sum([abs(l-r) for l, r in zip(left, right)])
print(sum_of_distances)
