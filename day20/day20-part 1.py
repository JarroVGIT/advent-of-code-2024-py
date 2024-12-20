# Advent of Code 2024 - Day 20 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_grid, start_time, print_grid
from rich import print

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

cheats: list[tuple[complex, complex, int]] = []
for loc, val in grid.items():
    if val == ".":
        continue
    track_ns = [loc+n for n in neighbors if grid.get(loc+n)=="."]
    if len(track_ns) >= 2:
        # sort the locations by occurence in track:
        track_ns.sort(key=lambda c: track.index(c))

        # there can be multiple cheats possible, e.g.
        # ...
        # .#.
        # .#.
        # you can go from 0,1 to 1,0, or from 0,1 to 2,1 or from 1,0 to 2,1.   
        # update; this doesn't seem to matter. Just take first and last in list.
        c_start = track_ns[0]
        c_end = track_ns[-1]
        c_len = c_len = track.index(c_end) - track.index(c_start) - 2
        cheats.append((c_start, c_end, c_len))
        # for i, c_start in enumerate(track_ns[:-1]):
        #     for c_end in track_ns[i+1:]:
        #         c_len = track.index(c_end) - track.index(c_start) + 2
        #         cheats.append((c_start, c_end, c_len))
c = [(s, e, l) for s,e,l in cheats if l >= 100]
c.sort(key=lambda c: c[2])

result = len(c)

print(f"Part 1: {result}, {elapsed(start_time)}")