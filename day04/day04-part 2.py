# Advent of Code 2024 - Day 04
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
#import re

#with open("./day04/example.txt") as f:
#with open("./day04/example-2.txt") as f:
with open("./day04/input.txt") as f:
    content = f.read().split("\n")

grid = {}
for y, row in enumerate(content):
    for x, val in enumerate(row):
        grid[complex(x,y)] = val

found = 0
for y in range(len(content)):
    for x, val in enumerate(content[y]):
        if val == "A":
            # A . B
            # . a . 
            # C . D
            a = grid.get(complex(x-1, y-1), " ")
            b = grid.get(complex(x+1, y-1), " ")
            c = grid.get(complex(x-1, y+1), " ")
            d = grid.get(complex(x+1, y+1), " ")
            if ((a=="M" and d=="S") or (a=="S" and d=="M")) and \
                ((b=="M" and c=="S") or (b=="S" and c=="M")):
                found += 1
        else: 
            continue

print(found)