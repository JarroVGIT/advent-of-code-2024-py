# Advent of Code 2024 - Day 05
# Author: Jarro van Ginkel
# Part 2

# Possible imports required:
from rich import print
from collections import defaultdict
from copy import copy
# import re

# with open("./day05/example.txt") as f:
# with open("./day05/example-2.txt") as f:
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

updates_list: list[list[int]] = []
for update in updates:
    update = list(map(int, update.split(",")))
    updates_list.append(update)
    if not len(update) == len(set(update)):
        print("update")


def move_wrong_to_right(
    orig_update: list[int], wrong_right: set[int], wrong_val_idx: int, wrong_val: int
) -> list[int]:
    highest_pos = 0
    for v in list(wrong_right):
        pos = update.index(v)
        highest_pos = max(highest_pos, pos)

    new_update = copy(orig_update)
    new_update.insert(highest_pos + 1, wrong_val)
    new_update.pop(wrong_val_idx)
    return new_update

wrong_updates: list[list[int]] = []

for update_idx, update in enumerate(updates_list):
    for val_idx, val in enumerate(update):
        right = set(update[val_idx + 1 :])
        rules_prior = rules_dict[val][0]
        # Actualy, the first incorrect value will never be wrong to the left, 
        # because it would have been flagged when we checked the values prior 
        # to this value.
        wrong_right = right & rules_prior
        if wrong_right:
            # violations in wrong_right mean we need to move this value to at least
            # the index of the last violation + 1.
            # Perform once and append to wrong_updates.
            new_update = move_wrong_to_right(update, wrong_right, val_idx, val)
            wrong_updates.append(new_update)
            break

result = 0

# Semi bruteforce; do the same logic again (checking each value on violations to the right),
# and if found, move the value to so it has no violations anymore. Add the new sequence to the
# list of lists that we are running through.
while wrong_updates:
    update = wrong_updates.pop(0)
    for val_idx, val in enumerate(update):
        right = set(update[val_idx + 1 :])
        rules_prior = rules_dict[val][0]
        wrong_right = right & rules_prior
        if wrong_right:
            new_update = move_wrong_to_right(update, wrong_right, val_idx, val)
            wrong_updates.append(new_update)
            break
    else:
        middle_idx = len(update) // 2
        result += update[middle_idx]

print(result)
