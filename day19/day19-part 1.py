# Advent of Code 2024 - Day 19 - part 1
# Author: Jarro van Ginkel
from rich import print
import time
from functools import lru_cache

#with open("./day19/example.txt") as f:
with open("./day19/input.txt") as f:
    towels, designs = f.read().split("\n\n")


def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

towels = towels.split(", ")
designs = designs.split("\n")

@lru_cache
def deconstruct(remaining_design:str) -> bool:
    if not remaining_design:
        return True
    for t in towels:
        if remaining_design.startswith(t):
            if deconstruct(remaining_design[len(t):]):
                return True
    return False 

result = 0

for design in designs:
    if deconstruct(design):
        result += 1

print(f"Part 1: {result}, {elapsed(start_time)}")