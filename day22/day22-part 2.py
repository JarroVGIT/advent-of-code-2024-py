# Advent of Code 2024 - Day 22 - part 2
# Author: Jarro van Ginkel
from rich import print
import time

with open("./day22/example.txt") as f:
#with open("./day22/input.txt") as f:
    content = f.read().split("\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()




result = 0

print(f"Part 2: {result}, {elapsed(start_time)}")