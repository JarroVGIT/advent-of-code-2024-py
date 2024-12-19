# Advent of Code 2024 - Day 19 - part 2
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
def deconstruct(remaining_design:str) -> int:
    if not remaining_design:
        return 1
    total_ways = 0
    for t in towels:
        if remaining_design.startswith(t):
            total_ways += deconstruct(remaining_design[len(t):])
    return total_ways 

result = 0

for design in designs:
    result +=deconstruct(design)

print(f"Part 2: {result}, {elapsed(start_time)}")