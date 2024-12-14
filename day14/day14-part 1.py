# Advent of Code 2024 - Day 14 - part 1
# Author: Jarro van Ginkel
from rich import print
import time
from collections import defaultdict

#with open("./day14/example.txt") as f:
with open("./day14/input.txt") as f:
    content = f.read().split("\n")

len_x = 101
len_y = 103

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

robots = {}
for idx, line in enumerate(content):
    p, v = line.split(" ")
    x, y = p.replace("p=", "").split(",")
    dx, dy = v.replace("v=", "").split(",")
    robots[idx] = {"x": int(x), "y": int(y), "dx": int(dx), "dy": int(dy)}

locs = defaultdict(lambda:0)
for robot, f in robots.items():
    new_x = (f["x"] + 100 * f["dx"]) % len_x
    new_y = (f["y"] + 100 * f["dy"]) % len_y
    locs[(new_x, new_y)] += 1

q1, q2, q3, q4 = 0, 0, 0, 0

for loc, count in locs.items():
    if loc[0] < len_x//2 and loc[1] < len_y//2:
        q1 += count
    elif loc[0] < len_x//2 and loc[1] > len_y//2:
        q2 += count
    elif loc[0] > len_x//2 and loc[1] < len_y//2:
        q3 += count
    elif loc[0] > len_x//2 and loc[1] > len_y//2:
        q4 += count
print(q1, q2, q3, q4)
result = q1 * q2 * q3 * q4

print(f"Part 1: {result}, {elapsed(start_time)}")