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

# track: list[complex] = [start]
# current_loc = start
# while current_loc != end:
#     for n in neighbors:
#         if current_loc+n not in track and grid.get(current_loc+n) == ".":
#             current_loc = current_loc+n
#             track.append(current_loc)

# # start, end, cheat-gain
cheats: list[tuple[complex, complex, int]] = []

# keep track of each distance from start rather than a list
# because map lookups are O(1) but list index finds are O(n).
# Runs in 2 seconds now.
track: dict[complex, int] = {start: 0}
current_loc = start
while current_loc != end:
    for n in neighbors:
        if current_loc+n not in track and grid.get(current_loc+n) == ".":
            track[current_loc+n] = track[current_loc] + 1
            current_loc = current_loc+n

for start, s_dis in track.items():
    for y in range(-20, 21, 1):
        allowable_x = 20-abs(y)
        for x in range(-allowable_x, allowable_x+1, 1):
            target = start + complex(x,y)
            if target not in track:
                continue
            c_gain = track[target] - s_dis - abs(x) - abs(y)
            if c_gain >= 100:
                cheats.append((start, target, c_gain))

# cheats of same lenght to same locs (but different paths) are considered the same cheat.
# for each element in track, get all places in < 20 manhattan distance, 
# if target tile is on track and more than 100 away on track, add to cheats.

# even better because you can skip the first 100 mext tiles (we want larger than that.)
# also, indexing is expensive, so calculate the index of target.
# still not great though, 17 seconds..
# for s_idx, start in enumerate(track):
#     for t_idx, target in enumerate(track[s_idx+100:]):
#         distance = target - start
#         manhattan_dis = abs(int(distance.imag)) + abs(int(distance.real))
#         if manhattan_dis <= 20:
#             c_gain = (t_idx+s_idx+100) - s_idx - manhattan_dis
#             if c_gain >= 100:
#                 cheats.append((start, target, c_gain))


# better method but still long runtime (1.31 min):
# for idx, start in enumerate(track):
#     for target in track[idx+1:]:
#         distance = target - start
#         manhattan_dis = abs(int(distance.imag)) + abs(int(distance.real))
#         if manhattan_dis <= 20:
#             c_gain = track.index(target) - idx - manhattan_dis
#             if c_gain >= 100:
#                 cheats.append((start, target, c_gain))

# inefficient method, 14min runtime:
# for track_tile in track:
#     seen = []
#     for y in range(-20, 21, 1):
#         allowable_x = 20-abs(y)
#         for x in range(-allowable_x, allowable_x+1, 1):
#             target = track_tile + complex(x,y)
#             if target not in track or target in seen:
#                 continue
#             seen.append(target)
#             c_gain = track.index(target) - track.index(track_tile) - abs(x) - abs(y)
#             if c_gain >= 100:
#                 cheats.append((track_tile, target, c_gain))

result = len(cheats)

print(f"Part 2: {result}, {elapsed(start_time)}")