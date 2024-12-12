# Advent of Code 2024 - Day 12 - part 1
# Author: Jarro van Ginkel
from rich import print
import time

#with open("./day12/example.txt") as f:
with open("./day12/input.txt") as f:
    content = f.read().split("\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

grid: dict[complex, str] = {}

for y, row in enumerate(content):
    for x, val in enumerate(row):
        grid[complex(x,y)] = val

neighbors = [complex(1,0), complex(0,1), complex(-1,0), complex(0, -1)]

seen = set()

def get_perim_area(loc: complex, val: str, seen: set[complex]):
    area = 1
    next_neighbors = [loc+n for n in neighbors if grid.get(loc+n)==val and loc+n not in seen]
    perim = 4-len([loc+n for n in neighbors if grid.get(loc+n)==val])
    seen.update(next_neighbors)
    for neigbor in next_neighbors:
        n_area, n_perim = get_perim_area(neigbor, val,seen)
        area += n_area
        perim += n_perim
    return area, perim

all_perim_area = []
for loc, val in grid.items():
    if loc in seen:
        continue
    seen.add(loc)
    total_perimeter, area = get_perim_area(loc, val, seen)
    all_perim_area.append((total_perimeter, area))


result = sum([comb[0]*comb[1] for comb in all_perim_area])

print(f"Part 1: {result}, {elapsed(start_time)}")