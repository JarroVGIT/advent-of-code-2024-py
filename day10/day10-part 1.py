# Advent of Code 2024 - Day 10 - part 1
# Author: Jarro van Ginkel
import time

from rich import print

#with open("./day10/example.txt") as f:
with open("./day10/input.txt") as f:
    content = f.read().split("\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

grid: dict[complex, int] = {}
zeros: list[complex] = []

for y, row in enumerate(content):
    for x, val in enumerate(row):
        grid[complex(x,y)] = int(val)
        if val == '0':
            zeros.append(complex(x,y))

directions = [complex(1,0), complex(0,1), complex(-1,0), complex(0, -1)]

def find_nines(current_loc: complex, current_val: int, found: set) -> set[complex]:
    if current_val == 9:
        f = found
        f.add(current_loc)
        return f 
    result = set()
    for dir in directions:
        neighbor = current_loc + dir
        neighbor_val = grid.get(neighbor)
        if neighbor_val == current_val+1:
            res = find_nines(neighbor, neighbor_val, found)
            result = found.union(res)
    return result

result = 0

for zero in zeros:
    result += len(find_nines(zero, 0, set()))


print(f"Part 1: {result}, {elapsed(start_time)}")