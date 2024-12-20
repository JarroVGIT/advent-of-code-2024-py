# Advent of Code 2024 - Day 20 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_grid, start_time, print_grid
from rich import print
from itertools import groupby
grid = parse_data_as_grid(20)

start = min(k for k, v in grid.items() if v == "S")
end = min(k for k, v in grid.items() if v == "E")
grid[start] = "."
grid[end] = "."

neighbors = [complex(0,-1), complex(1, 0), complex(0,1), complex(-1,0)]

track = [start]
current_loc = start
while current_loc != end:
    for n in neighbors:
        if current_loc+n not in track and grid.get(current_loc+n) == ".":
            current_loc = current_loc+n
            track.append(current_loc)

# start, end, cheat-gain
cheats: list[tuple[complex, complex, int]] = []

# cheats of same lenght to same locs (but different paths) are considered the same cheat.
# for each element in track, get all places in < 20 manhattan distance, 
# if target tile is on track and more than 100 away on track, add to cheats.

for track_tile in track:
    seen = []
    for y in range(-20, 21, 1):
        allowable_x = 20-abs(y)
        for x in range(-allowable_x, allowable_x+1, 1):
            target = track_tile + complex(x,y)
            if target not in track or target in seen:
                continue
            seen.append(target)
            c_gain = track.index(target) - track.index(track_tile) - abs(x) - abs(y)
            if c_gain >= 100:
                cheats.append((track_tile, target, c_gain))

# cheats.sort(key=lambda c: c[2])                
# c = groupby(cheats, key=lambda c: c[2])
# for key, group in c:
#     print(key, len(list(group)))
# print(cheats[-1])
result = len(cheats)

print(f"Part 2: {result}, {elapsed(start_time)}")