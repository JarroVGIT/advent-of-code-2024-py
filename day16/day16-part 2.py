# Advent of Code 2024 - Day 16 - part 2
# Author: Jarro van Ginkel
from rich import print
import time
import networkx as nx

#with open("./day16/example.txt") as f:
with open("./day16/input.txt") as f:
    content = f.read().split("\n")


def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"


start_time = time.time()

grid = {}
max_y = len(content)
max_x = len(content[0])

for y, row in enumerate(content):
    for x, val in enumerate(row):
        grid[complex(x, y)] = val
        if val == "S":
            start_loc = complex(x, y)
        if val == "E":
            target = complex(x, y)

neighbors = {
    "v": {"v": complex(0, 1), "<": complex(-1, 0), ">": complex(1, 0)},
    "<": {"<": complex(-1, 0), "^": complex(0, -1), "v": complex(0, 1)},
    "^": {"^": complex(0, -1), "<": complex(-1, 0), ">": complex(1, 0)},
    ">": {">": complex(1, 0), "^": complex(0, -1), "v": complex(0, 1)},
}

G = nx.DiGraph()

for loc, val in grid.items():
    for dir, ns in neighbors.items():
        current_node = (loc, dir)
        for ndir, nloc in ns.items():
            next_loc = loc+nloc
            if grid.get(next_loc, "#") == "#":
                continue
            if next_loc == target:
                next_node = target
            else:
                next_node = (next_loc, ndir)
            if dir == ndir:
                G.add_edge(current_node, next_node, cost=1)
            else:
                G.add_edge(current_node, next_node, cost=1001)

paths = nx.all_shortest_paths(G, (start_loc, ">"), target, weight="cost")

locs = set()

for path in paths:
    for loc in path:
        if isinstance(loc, tuple):
            locs.add(loc[0])
        else:
            locs.add(loc)

result = len(locs)

print(f"Part 2: {result}, {elapsed(start_time)}")