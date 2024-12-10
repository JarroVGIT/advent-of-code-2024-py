# Advent of Code 2024 - Day 10 - part 1
# Author: Jarro van Ginkel
from rich import print
import time

with open("./day10/example.txt") as f:
#with open("./day10/input.txt") as f:
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

def find_nines(curent_loc: complex, current_val: int) -> int:
    if current_val == 9:
        return 1
    result = 0
    for dir in directions:
        neighbour = curent_loc + dir
        neighbour_val = grid.get(neighbour)
        if neighbour_val == current_val+1:
            result += find_nines(neighbour, current_val+1)
    return result

result = 0

for zero in zeros:
    result += find_nines(zero, 0)


print(f"Part 1: {result}, {elapsed(start_time)}")