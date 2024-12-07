# Advent of Code 2024 - Day 07
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
#import re
import time
from itertools import product
from typing import Callable

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

#with open("./day07/example.txt") as f:
with open("./day07/input.txt") as f:
    content = f.read().split("\n")

start_time = time.time()
result = 0

lines = []
for line in content:
    outcome, components = line.split(":")
    outcome = int(outcome)
    components = list(map(int, components.split()))
    lines.append((outcome, components))

def mul(a:int, b:int) -> int:
    return a * b

def add(a:int, b:int) -> int:
    return a + b

def join(a:int, b:int) -> int:
    return int(str(a)+str(b))

def calc_combi(lh: int, components: list[int], operations: list[Callable]):
    if len(operations)>0:
        opp = operations[0]
        res = opp(lh, components[0])
        return calc_combi(res, components[1:], operations[1:])
    else:
        return lh

for outcome, components in lines:
    combinations = list(product([mul, add, join], repeat=len(components)-1))
    for operations in combinations:
        calculation = calc_combi(components[0], components[1:], operations)
        if calculation == outcome:
            result += outcome
            break

print(f"Part 2: {result}, {elapsed(start_time)}")
