# Advent of Code 2024 - Day 05
# Author: Jarro van Ginkel
# Part 1

# Possible imports required:
from rich import print
from collections import defaultdict
#import re

#with open("./day05/example.txt") as f:
with open("./day05/input.txt") as f:
    content = f.read().split("\n\n")

rules = content[0].split("\n")
updates = content[1].split("\n")
# tuple holding (0) numbers that can only be prior and (1) numbers that can only be after. 
rules_dict: dict[int, tuple[set[int], set[int]]] = defaultdict(lambda: (set(), set()))
for rule in rules:
    l, r = list(map(int, rule.split("|")))
    rules_dict[l][1].add(r)
    rules_dict[r][0].add(l)

result = 0
for update in updates:
    update = list(map(int, update.split(",")))
    for idx, val in enumerate(update):
        left = set(update[:idx])
        right = set(update[idx+1:])
        rules_prior = rules_dict[val][0]
        rules_after = rules_dict[val][1]
        # None of the left can occur in the dict 'after' set
        # None of the right can occur in the dict 'prior' set
        if (left & rules_after) | (right & rules_prior):
            break
    else:
        middle_idx = len(update)//2
        result += update[middle_idx]
print(result)



