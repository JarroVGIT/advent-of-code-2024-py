# Advent of Code 2024 - Day 04
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
from rich import print
#import re

#with open("./day04/example.txt") as f:
with open("./day04/input.txt") as f:
    content = f.read().split("\n")

grid = {}
xs = []
for y, row in enumerate(content):
    for x, val in enumerate(row):
        grid[complex(x,y)] = val
        if val == "X":
            xs.append(complex(x,y))

directions = [
    [complex(1,0), complex(2,0),complex(3,0)],
    [complex(1,1), complex(2,2),complex(3,3)],
    [complex(0,1), complex(0,2),complex(0,3)],
    [complex(-1,1), complex(-2,2),complex(-3,3)],
    [complex(-1,0), complex(-2,0),complex(-3,0)],
    [complex(-1,-1), complex(-2,-2),complex(-3,-3)],
    [complex(0,-1), complex(0,-2),complex(0,-3)],
    [complex(1,-1), complex(2,-2),complex(3,-3)],
]
found = 0
found_coords = set()
for xloc in xs:
    for direction in directions:
        s = "X"
        for next_coord in direction:
            next_val = grid.get(xloc+next_coord, " ")
            s = s + next_val
        if s == "XMAS":
            found += 1

print(found)


