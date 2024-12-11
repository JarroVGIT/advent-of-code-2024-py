# Advent of Code 2024 - Day 11 - part 1
# Author: Jarro van Ginkel
from rich import print
import time

# with open("./day11/example.txt") as f:
# #with open("./day11/input.txt") as f:
#     content = f.read().split("\n")

#content = ["125", "17"]
content = ["112", "1110", "163902", "0", "7656027", "83039", "9", "74"]

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

# This is going to be inefficient but so be it.
def flatten(lst: list):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

li = []
for item in content:
    li.append([int(item)])

for idx in range(len(li)):
    for _ in range(75):
        orig_list = li[idx]
        for i, val in enumerate(orig_list):
            if val == 0:
                orig_list[i] = 1
            elif (length:=len(str(val)))%2 == 0:
                left = int(str(val)[:(length//2)])
                right = int(str(val)[(length//2):])
                orig_list[i] = [left, right]
            else:
                orig_list[i] = val*2024
            
        # Flatten
        li[idx] = flatten(orig_list)


result = sum(len(i) for i in li)

print(f"Part 1: {result}, {elapsed(start_time)}")