# Advent of Code 2024 - Day 08
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
#import re
import time
from collections import defaultdict
from itertools import combinations

#with open("./day08/example.txt") as f:
#with open("./day08/example-2.txt") as f:
with open("./day08/input.txt") as f:
    content = f.read().split("\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

start_time = time.time()

grid: dict[str, list[complex]] = defaultdict(list)

for y, row in enumerate(content):
    for x, val in enumerate(row):
        if val != ".":
            grid[val].append(complex(x,y))

def is_in_grid(loc: complex, min_x=0, max_x=len(content[0])-1, min_y=0, max_y=len(content)-1) -> bool:
    return int(loc.real) >= min_x and \
    int(loc.real) <= max_x and \
    int(loc.imag) >= min_y and \
    int(loc.imag) <= max_y

antinodes = set()
for val, locs in grid.items():
    # create all possible pairs
    combis = list(combinations(locs, 2))
    for point_a, point_b in combis:
        antinodes.add(point_a)
        antinodes.add(point_b)

        # can safely ignore direction, as both antennas are antinode locations too.
        diff = point_a-point_b
        new_point_1 = point_a-diff
        while is_in_grid(new_point_1):
            antinodes.add(new_point_1)
            new_point_1 = new_point_1 - diff
        
        new_point_2 = point_a + diff
        while is_in_grid(new_point_2):
            antinodes.add(new_point_2)
            new_point_2 = new_point_2 + diff


result = len(antinodes)
print(f"Part 2: {result}, {elapsed(start_time)}")
