# Advent of Code 2024 - Day 21 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
import networkx as nx

content = parse_data_as_lines(21)

numpad = nx.Graph()
numpad.add_edges_from([(7,8), (7,4), (8,9), (8,5), (9,6), (6,5), (6,3), (5,4), (5,2)
                             (4,1), (1,2), (2,3), (2,0), (3, "A"), ("A", 0)])
dir_pad1 = nx.Graph()
dir_pad1.add_edges_from([("A", "^"), ("A", ">"), ("^", "v"), (">", "v"), ("v", "<")])

dir_pad2 = nx.Graph()
dir_pad2.add_edges_from([("A", "^"), ("A", ">"), ("^", "v"), (">", "v"), ("v", "<")])


result = 0

print(f"Part 1: {result}, {elapsed(start_time)}")