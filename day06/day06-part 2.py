# Advent of Code 2024 - Day 06
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
#import re

#with open("./day06/example.txt") as f:
#with open("./day06/example-2.txt") as f:
with open("./day06/input.txt") as f:
    content = f.read().split("\n")


grid: dict[complex, str]= {}
current_loc: complex
 
for y, row in enumerate(content):
    for x, val in enumerate(row):
        if val == "^":
            current_loc = complex(x,y)
            starting_loc = current_loc
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

# We have a list of all possible locations a new rock can be placed.
# Add each location one by one to the obstruction list, re-run pattern.
# Store used location with direction, if already exists its a loop.
obstructions_causing_loop = []
orig_used_locations = list(set(used_locations))
for possible_obstruction in orig_used_locations:
    if possible_obstruction == starting_loc:    
        # Don't test the starting location
        continue
    
    direction = "^"
    current_loc = starting_loc
    used_locations = [(current_loc, direction)]
    loop_found = True

    grid[possible_obstruction] = "#"
    while True:
        next_loc = current_loc + neighbour[direction]

        # Reached end of grid
        if int(next_loc.real) < min_x or \
            int(next_loc.real) > max_x or \
            int(next_loc.imag) < min_y or \
            int(next_loc.imag) > max_y:
            loop_found = False
            break
        
        # Obstruction, rotate and don't move
        if next_loc in grid:
            direction = next_direction[direction]
        else:
            current_loc = next_loc
            if (current_loc, direction) not in used_locations:
                used_locations.append((current_loc, direction))
            else:
                # loop found, yay
                break
    
    if loop_found:
        obstructions_causing_loop.append(possible_obstruction)
        
    grid.pop(possible_obstruction)
    
print(len(obstructions_causing_loop))
