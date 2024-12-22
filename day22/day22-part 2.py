# Advent of Code 2024 - Day 22 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from collections import defaultdict, deque

content = parse_data_as_lines(22)
result = 0

def calc(x: int) -> int:
    m = 16777216 - 1
    x = (x ^ (x << 6)) & m
    x = (x ^ (x >> 5)) & m
    x = (x ^ (x << 11)) & m
    return x

# bruteforce? Store all sequences as tuples and add the amount of banasas it would yield. 
seq = defaultdict(int)
for line in content:
    num = int(line)
    last = num % 10
    changes = deque([])
    seq_seen = set()
    for i in range(2000):
        num = calc(num)
        last_digit = num % 10
        changes.append(last_digit - last)
        if len(changes) == 4:
            t = tuple(changes)
            if t not in seq_seen:
                seq[t] += last_digit
                seq_seen.add(t)
            else:
                pass
            changes.popleft()
        last = last_digit

count = 0
sequence = None
for k, v in seq.items():
    if v > count:
        count = v
        sequence = k
result = count

print(f"Part 2: {result}, {elapsed(start_time)}")