# Advent of Code 2024 - Day 09
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
from rich import print
#import re
import time 
import copy

#with open("./day09/example.txt") as f:
with open("./day09/input.txt") as f:
    content = f.read().split("\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

start_time = time.time()

disk = []
total = 0
for idx, number in enumerate(content[0]):
    if idx % 2 == 0:
        file_index = ((idx+2) // 2) - 1
        disk += [file_index]*int(number)
    else:
        disk += [None]*int(number)
    total += int(number)

back_search_idx = -1
fwd_search_idx = 0

for idx in range(len(disk)):
    if (len(disk) + back_search_idx) <= fwd_search_idx:
        break
    if disk[back_search_idx] is None: # None in the back
        back_search_idx -= 1
        continue
    if disk[fwd_search_idx] is not None: # Number in the front
        fwd_search_idx += 1
    else: # Replace None in the front with val in the back
        disk[fwd_search_idx] = disk[back_search_idx]
        disk[back_search_idx] = None
        fwd_search_idx += 1
        back_search_idx -= 1

result = 0

for idx, val in enumerate(disk):
    if val is None:
        break
    result += idx*val

print(f"Part 1: {result}, {elapsed(start_time)}")