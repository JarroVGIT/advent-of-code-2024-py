# Advent of Code 2024 - Day 09
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
#import re
import time

with open("./day09/example.txt") as f:
#with open("./day09/example-2.txt") as f:
#with open("./day09/input.txt") as f:
    content = f.read().split("\n")



def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

start_time = time.time()