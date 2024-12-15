# Advent of Code 2024 - Day 15 - part 2
# Author: Jarro van Ginkel
from rich import print
import time

with open("./day15/example.txt") as f:
#with open("./day15/input.txt") as f:
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


result = 0

print(f"Part 2: {result}, {elapsed(start_time)}")