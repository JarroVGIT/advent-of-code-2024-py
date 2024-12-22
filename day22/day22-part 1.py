# Advent of Code 2024 - Day 22 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(22)
result = 0

# The operations are rewriteable in bitwise operations:
# * 64 == << 5, // 32 == >> 4 and * 2048 == << 11
# 16777216 == 2^24 (the 25t bit is 1, everything else 0). 
# A modulos of a number as such can be bitwise computed as
# performing AND on 2^24 - 1 (all 24 least significant bits are 1), because
# every bit after (more significant) is a multiple of 2^24. 
# This can maybe even more shortened, but I don't know how; the XOR seems to depend
# on the previous step?

def calc(x: int) -> int:
    m = 16777216 - 1
    x = (x ^ (x << 6)) & m
    x = (x ^ (x >> 5)) & m
    x = (x ^ (x << 11)) & m
    return x

for line in content:
    num = int(line)
    for _ in range(2000):
        num = calc(num)
    result += num

print(f"Part 1: {result}, {elapsed(start_time)}")