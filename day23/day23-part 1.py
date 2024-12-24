# Advent of Code 2024 - Day 23 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from collections import defaultdict

content = parse_data_as_lines(23)

connections: dict[str, set[str]] = defaultdict(set)

for connection in content:
    lhs, rhs = connection.split("-")
    connections[lhs].add(rhs)
    connections[rhs].add(lhs)

three_conns: set[frozenset[str]] = set()

for computer, conns in connections.items():
    for conn in conns:
        intersect = list(conns.intersection(connections[conn]))
        if len(intersect) >= 1:
            for ins in intersect:
                if computer.startswith("t") or conn.startswith("t") or ins[0].startswith("t"):
                    three_conns.add(frozenset([computer, conn, ins]))


result = len(three_conns)

print(f"Part 1: {result}, {elapsed(start_time)}")