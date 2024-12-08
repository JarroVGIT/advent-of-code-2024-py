# Advent of Code 2024 - Day 08
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
from rich import print
#import re
import time
from collections import defaultdict
from itertools import combinations

#with open("./day08/example.txt") as f:
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
        diff = point_a - point_b
        
        d_x = abs(int(diff.real))
        if point_a.real > point_b.real:
            new_point_1 = complex(point_a.real + d_x, 0)
            new_point_2 = complex(point_b.real - d_x, 0)
        elif point_b.real > point_a.real:
            new_point_1 = complex(point_a.real - d_x, 0)
            new_point_2 = complex(point_b.real + d_x, 0)
        else:
            new_point_ = complex(point_a.real, 0)
            new_point_2 = complex(point_a.real, 0)
        
        d_y = abs(int(diff.imag))
        if point_a.imag > point_b.imag:
            new_point_1 += complex(0, point_a.imag + d_y)
            new_point_2 += complex(0, point_b.imag - d_y)
        elif point_b.imag > point_a.imag:
            new_point_1 += complex(0, point_a.imag - d_y)
            new_point_2 += complex(0, point_b.imag + d_y)
        else:
            new_point_1 += complex(0, point_a.imag)
            new_point_2 += complex(0, point_a.imag)

        if is_in_grid(new_point_1):
            antinodes.add(new_point_1)
        if is_in_grid(new_point_2):
            antinodes.add(new_point_2)


result = len(antinodes)
print(f"Part 1: {result}, {elapsed(start_time)}")
