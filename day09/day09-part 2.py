# Advent of Code 2024 - Day 09
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
#import re
import time

from rich import print

#with open("./day09/example.txt") as f:
#with open("./day09/example-2.txt") as f:
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
for idx, number in enumerate(content[0]):
    if idx % 2 == 0:
        file_index = ((idx+2) // 2) - 1
        disk.append([file_index]*int(number))
    else:
        disk.append([None]*int(number))

for back_idx in range(len(disk)-1, 0, -1):
    if len(disk[back_idx]) > 0 and disk[back_idx][0] is not None:
        for fwd_idx in range(0, len(disk), 1):
            if fwd_idx == back_idx:
                break
            if len(disk[fwd_idx]) > 0 and disk[fwd_idx][0] is None:
                if len(disk[back_idx]) <= len(disk[fwd_idx]):
                    rest = [None] * (len(disk[fwd_idx])-len(disk[back_idx]))
                    disk[fwd_idx] = disk[back_idx]
                    disk[back_idx] = [None] * len(disk[back_idx])
                    if rest:
                        disk.insert(fwd_idx + 1, rest)
                    break

result = 0

disk = [i for part in disk for i in part]
for idx, val in enumerate(disk):
    if val is None:
        continue
    result += idx*val

print(f"Part 2: {result}, {elapsed(start_time)}")