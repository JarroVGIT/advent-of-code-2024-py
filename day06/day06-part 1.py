# Advent of Code 2024 - Day 06
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
from rich import print
#import re

#with open("./day06/example.txt") as f:
with open("./day06/input.txt") as f:
    content = f.read().split("\n")

grid: dict[complex, str]= {}
current_loc: complex
 
for y, row in enumerate(content):
    for x, val in enumerate(row):
        if val == "^":
            current_loc = complex(x,y)
            continue
        if val != ".":
            grid[complex(x,y)] = val

min_x, min_y = 0, 0
max_x = len(content[0])-1
max_y = len(content)-1

used_locations = [current_loc]
neighbour = {
    "^": complex(0, -1),
    ">": complex(1, 0),
    "v": complex(0, 1),
    "<": complex(-1, 0)
}
next_direction = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

direction = "^"
while True:
    next_loc = current_loc + neighbour[direction]

    # Reached end of grid
    if int(next_loc.real) < min_x or \
        int(next_loc.real) > max_x or \
        int(next_loc.imag) < min_y or \
        int(next_loc.imag) > max_y:
        break
    
    # Obstruction, rotate and don't move
    if next_loc in grid:
        direction = next_direction[direction]
    else:
        current_loc = next_loc
        used_locations.append(next_loc)


print(len(set(used_locations)))
    
