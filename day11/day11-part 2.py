# Advent of Code 2024 - Day 11 - part 2
# Author: Jarro van Ginkel
import copy
import time
from collections import defaultdict
from functools import lru_cache

from rich import print

# with open("./day11/example.txt") as f:
# #with open("./day11/input.txt") as f:
#     content = f.read().split("\n")

#content = ["125", "17"]
content = ["112", "1110", "163902", "0", "7656027", "83039", "9", "74"]
# content = ["0"]
def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()


@lru_cache()
def get_next_value(val: int) -> list[int]:
    if val == 0:
        return [1]
    elif (length:=len(str(val)))%2 == 0:
        left = int(str(val)[:(length//2)])
        right = int(str(val)[(length//2):])
        return [left, right]
    else:
        return [val*2024]

# keep track of counts of numbers
count_of_numbers: dict[int, int] = defaultdict(lambda: 0)
for item in content:
    count_of_numbers[int(item)] += 1


for loop in range(75):
    numbers = defaultdict(lambda: 0)
    for number, count in count_of_numbers.items():
        next_val = get_next_value(number)
        for next in next_val:
            numbers[next] += count
    count_of_numbers = copy.copy(numbers)


result = sum(v for _,v in count_of_numbers.items())

print(f"Part 2: {result}, {elapsed(start_time)}")