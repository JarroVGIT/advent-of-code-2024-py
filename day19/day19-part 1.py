# Advent of Code 2024 - Day 19 - part 1
# Author: Jarro van Ginkel
from functools import lru_cache

from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

towels, designs = parse_data_as_lines(19, "\n\n")

towels = towels.split(", ")
designs = designs.split("\n")


@lru_cache
def deconstruct(remaining_design: str) -> bool:
    if not remaining_design:
        return True
    for t in towels:
        if remaining_design.startswith(t):
            if deconstruct(remaining_design[len(t) :]):
                return True
    return False


result = 0

for design in designs:
    if deconstruct(design):
        result += 1

print(f"Part 1: {result}, {elapsed(start_time)}")
