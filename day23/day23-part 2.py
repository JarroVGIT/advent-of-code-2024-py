# Advent of Code 2024 - Day 23 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
import networkx as nx

content = parse_data_as_lines(23)
result = 0
G = nx.Graph()
for connection in content:
    lhs, rhs = connection.split("-")
    G.add_edge(lhs, rhs)

cliques = list(nx.enumerate_all_cliques(G))[-1]
cliques.sort()

result = ",".join(cliques)
print(f"Part 2: {result}, {elapsed(start_time)}")