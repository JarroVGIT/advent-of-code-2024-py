# Advent of Code 2024 - Day 06
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
#import re
import time
def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

#with open("./day06/example.txt") as f:
#with open("./day06/example-2.txt") as f:
with open("./day06/input.txt") as f:
    content = f.read().split("\n")

start_time = time.time()

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

def is_exit(location: complex, min_y=min_y, max_y=max_y, min_x=min_x, max_x=max_x) -> bool:
    return int(location.real) < min_x or \
        int(location.real) > max_x or \
        int(location.imag) < min_y or \
        int(location.imag) > max_y

direction = "^"

# build up original paths taken:
used_locs_orig: list[complex] = [current_loc]
used_locs_dirs_orig: list[tuple[complex, str]] = [(current_loc, direction)]
while True:
    next_loc = current_loc + neighbour[direction]
    # Reached end of grid
    if is_exit(next_loc):
        break
    
    # Obstruction, rotate and don't move
    if next_loc in grid:
        direction = next_direction[direction]
    else:
        current_loc = next_loc
        used_locs_orig.append(current_loc)
        used_locs_dirs_orig.append((current_loc, direction))

# We have a list of all possible locations a new rock can be placed.
# Add each location one by one to the obstruction list, re-run pattern.
# Store used location with direction, if already exists its a loop.
print(f"Part 1: {len(set(used_locs_orig))}, {elapsed(start_time)}")
start_time = time.time()

# store the result.
locs_causing_loops = []

# only check the first loc in loc,dir combinations 
checked_new_locs = []

for idx, (obstr_location, direction) in enumerate(used_locs_dirs_orig):
    if obstr_location == starting_loc:
        # can't place obstruction in starting position, skip.
        continue
    
    if obstr_location in checked_new_locs:
        # don't re-check locations with different directions; in earlier passage
        # this location would have impacted path so far.
        continue
    else:
        checked_new_locs.append(obstr_location)
    # start off in the previous location.
    current_loc = obstr_location - neighbour[direction]
    grid[obstr_location] = "#"
    iter_used_locs_dirs = used_locs_dirs_orig[:idx]
    loop_found = True

    while True:
        next_loc = current_loc + neighbour[direction]
        if is_exit(next_loc):
            loop_found = False
            break
        if next_loc in grid:
            direction = next_direction[direction]
        else:
            current_loc = next_loc
            if (current_loc, direction) not in iter_used_locs_dirs:
                iter_used_locs_dirs.append((current_loc, direction))
            else:
                break
    if loop_found:
        locs_causing_loops.append(obstr_location)
        
    grid.pop(obstr_location)

print(f"Part 2: {len(locs_causing_loops)}, ({elapsed(start_time)})")