# Advent of Code 2024 - Day 15 - part 2
# Author: Jarro van Ginkel
from rich import print
import time

#with open("./day15/example.txt") as f:
with open("./day15/input.txt") as f:
    field, moves = f.read().split("\n\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

# idea: creation of grid is doable, still create grid in 
# dict, so with complex(x,y) = "[" etc. When moving, up or down
# think in list of ranges. If the direct above is [, then look up on 
# the range with the accompanying ]. If overlap is half (e.g ] of a box is on 
# top of [ of the box directly above, redo the while loop but with a list of
# ranges to keep track what to check next. If all ranges have a . above then, then
# move everything up 1. If one has a #, then no move. left/right has no impact. 
# list of ranges required in case you run into V form of boxes; a # in the middle 
# should not halt the entire box structure.

grid = {}
max_y = len(field.split("\n"))
max_x = len(field.split("\n")[0])*2

for y, row in enumerate(field.split("\n")):
    for x, val in enumerate(row):
        x1 = x*2
        x2 = x1 + 1
        if val == "O":
            grid[complex(x1,y)] = "["
            grid[complex(x2,y)] = "]"
        elif val == "@":
            grid[complex(x1,y)] = "@"
            grid[complex(x2,y)] = "."
            current_loc = complex(x1,y)
        else:
            grid[complex(x1,y)] = val
            grid[complex(x2,y)] = val        

def print_grid():
    for y in range(max_y):
        row = ""
        for x in range(max_x):
            row += grid[complex(x,y)]
        print(row)


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
    if next_val == ".":
        grid[current_loc] = "."
        grid[neighbor] = "@"
        current_loc = neighbor
    elif next_val == "#":
        continue
    elif move in ["v", "^"]:
        # only for up or down.
        next_loc = neighbor
        locs_to_move: list[list[complex]] = []
        if next_val == "[":
            locs_to_move.append([neighbor, neighbor + complex(1,0)])
        else:
            locs_to_move.append([neighbor + complex(-1,0), neighbor])
        while True:
            # check each next block, adding to the locs to move untill hitting stone.
            new_locs_to_move = []
            found_stone = False
            check_locs = locs_to_move[-1]
            for loc in check_locs:
                n_neighbor, n_val = get_next_val(move, loc)
                if n_val == ".":
                    continue
                elif n_val == "#":
                    found_stone = True
                    break
                elif n_val in ["[", "]"]:
                    if n_val == "[":
                        new_locs_to_move.extend([n_neighbor, n_neighbor + complex(1,0)])
                    else:
                        new_locs_to_move.extend([n_neighbor + complex(-1,0), n_neighbor])
            if new_locs_to_move and not found_stone:
                # start new iteration with next found boxes.
                locs_to_move.append(list(set(new_locs_to_move)))
                continue
            elif not new_locs_to_move and not found_stone:
                # all locs to move are free to move up one spot.
                locs_to_move.reverse()
                for locs in locs_to_move:
                    for loc in locs:
                        grid[loc+directions[move]] = grid[loc]
                        grid[loc] = "."
                # finally move the robot.
                grid[current_loc] = "."
                grid[next_loc] = "@"
                current_loc = next_loc
                break
            else:
                # found stone, no move.
                break
    else:
        # found box, move horizontal.
        next_loc = neighbor
        found_stone = False
        locs_passed = [neighbor]
        while True:
            neighbor, next_val = get_next_val(move, neighbor)
            if next_val in ["[", "]"]:
                locs_passed.append(neighbor)
                continue
            elif next_val == ".":
                break
            else: # found rock
                found_stone = True
                break
        if not found_stone:
            # move whole row
            locs_passed.reverse()
            for loc in locs_passed:
                grid[loc+directions[move]] = grid[loc]
                grid[loc] = "."
            grid[current_loc] = "."
            grid[next_loc] = "@"
            current_loc = next_loc

result = 0

for y in range(max_y):
    for x in range(max_x):
        if grid[complex(x,y)] == "[":
            result += x + 100*y

print(f"Part 2: {result}, {elapsed(start_time)}")