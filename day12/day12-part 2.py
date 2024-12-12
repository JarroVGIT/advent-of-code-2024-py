# Advent of Code 2024 - Day 12 - part 2
# Author: Jarro van Ginkel
from rich import print
import time

#with open("./day12/example.txt") as f:
with open("./day12/input.txt") as f:
    content = f.read().split("\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

grid: dict[complex, str] = {}

for y, row in enumerate(content):
    for x, val in enumerate(row):
        grid[complex(x,y)] = val

neighbors = [complex(1,0), complex(0,1), complex(-1,0), complex(0, -1)]

# a corner is when two adjecent sides of a block have not the same value as the block.
# inside corner: diagonal = same val, shared neighbor = same val. 
# CCCCC
# CAAAC
# CABAC
# CAAAC
# CCCCC
# 0,0 is corner (inside) because side + side but not in between (r1, c1)
# 0,0 is corner (outside) because right+upper =! left+down (r0, c0)
# 1,1 is corner because upper and left are different than self.
# Easier: for each block, create set of side that does not touch other same val?
# update: that is easier but also incorrect, doesn't account for more than one side
# on a row or col. Corner counting (inside + outside), then divide all corners by two

outside_corners = [ # corner = if val != [0].val != [1].val
    (complex(-1, 0), complex(0,-1)),
    (complex(0, -1), complex(1,0)),
    (complex(1, 0), complex(0,1)),
    (complex(0, 1), complex(-1,0)),
]

inside_corners = [ # corner = if val == [0].val and [1].val and [2].val != val
    (complex(-1, 0), complex(0,-1), complex(-1,-1)),
    (complex(0, -1), complex(1,0), complex(1,-1)),
    (complex(1, 0), complex(0,1), complex(1,1)),
    (complex(0, 1), complex(-1,0), complex(-1,1)),
]

def get_perim_area(loc: complex, val: str, seen: set[complex], corners: int):
    area = 1
    for c1, c2 in outside_corners:
        if grid.get(loc+c1) != val and grid.get(loc+c2) != val:
            corners += 1
    for c1, c2, diag in inside_corners:
        if grid.get(loc+c1) == val and grid.get(loc+c2) == val and grid.get(loc+diag) != val:
            corners += 1
    next_neighbors = [loc+n for n in neighbors if grid.get(loc+n)==val and loc+n not in seen]
    seen.update(next_neighbors)
    for neigbor in next_neighbors:
        n_area, corners = get_perim_area(neigbor,val,seen, corners)
        area += n_area
    return area, corners

seen = set()
sides_areas = []

for loc, val in grid.items():
    if loc in seen:
        continue
    seen.add(loc)
    area, corners= get_perim_area(loc, val, seen, 0)
    sides_areas.append((corners, area))


result = sum([combi[0]*combi[1] for combi in sides_areas])

print(f"Part 2: {result}, {elapsed(start_time)}")