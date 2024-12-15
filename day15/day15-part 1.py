# Advent of Code 2024 - Day 15 - part 1
# Author: Jarro van Ginkel
from rich import print
import time

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

#with open("./day15/example.txt") as f:
with open("./day15/input.txt") as f:
    field, moves = f.read().split("\n\n")

grid = {}
max_y = len(field.split("\n"))
max_x = len(field.split("\n")[0])

for y, row in enumerate(field.split("\n")):
    for x, val in enumerate(row):
        grid[complex(x,y)] = val
        if val == "@":
            current_loc = complex(x,y)

directions = {
    "v": complex(0, 1),
    "<": complex(-1, 0),
    "^": complex(0, -1),
    ">": complex(1, 0)
}

def get_next_val(dir: str, current_loc: complex) -> tuple[complex, str]:
    n = current_loc+directions[dir]
    return (n, grid.get(n))

for move in moves.replace("\n", ""):
    neighbor, next_val = get_next_val(move, current_loc)
    if next_val == "#":
        continue
    elif next_val == ".":
        grid[current_loc] = "."
        grid[neighbor] = "@"
        current_loc = neighbor
    elif next_val == "O":
        next_loc = neighbor
        found_stone = False
        while True:
            neighbor, next_val = get_next_val(move, neighbor)
            if next_val == "O":
                continue
            elif next_val == ".":
                break
            else: # found rock
                found_stone = True
                break
        if not found_stone:
            # only move entire row of boxes if the last found was not a rock.
            grid[neighbor] = "O"
            grid[current_loc] = "."
            current_loc = next_loc
            
result = 0

for y in range(max_y):
    for x in range(max_x):
        if grid[complex(x,y)] == "O":
            result += x + 100*y

print(f"Part 1: {result}, {elapsed(start_time)}")