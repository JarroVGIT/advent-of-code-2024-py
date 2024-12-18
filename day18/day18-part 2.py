# Advent of Code 2024 - Day 18 - part 2
# Author: Jarro van Ginkel
from rich import print
import time
import networkx as nx

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

start_time = time.time()

# with open("./day18/example.txt") as f:
#     content = f.read().split("\n")
#     grid_size = 6
#     byte_len = 12

with open("./day18/input.txt") as f:
    content = f.read().split("\n")
    grid_size = 70
    byte_len = 1024

b = []
for i in range(byte_len):
    x, y = map(int,content[i].split(","))
    b.append(complex(x, y))

directions = [complex(1, 0), complex(0, 1), complex(-1, 0), complex(0, -1)]

G = nx.DiGraph()

for y in range(grid_size + 1):
    for x in range(grid_size + 1):
        for n in directions:
            neighbor = complex(x, y) + n
            if (
                neighbor.real >= 0
                and neighbor.real <= grid_size
                and neighbor.imag >= 0
                and neighbor.imag <= grid_size
                and neighbor not in b
            ):
                G.add_edge(complex(x, y), neighbor)
s = complex(0,0)
t = complex(grid_size, grid_size)

# remove edges
for i in range(byte_len+1, len(content)):
    x, y = map(int,content[i].split(","))
    G.remove_node(complex(x,y))
    try:
        path = list(nx.shortest_path(G,s,t))
    except nx.NetworkXNoPath:
        result = content[i]
        break

print(f"Part 2: {result}, {elapsed(start_time)}")