# Advent of Code 2024 - Day 14 - part 2
# Author: Jarro van Ginkel
from rich import print
import time
from collections import defaultdict

#with open("./day14/example.txt") as f:
with open("./day14/input.txt") as f:
    content = f.read().split("\n")

len_x = 101
len_y = 103

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

robots = {}
for idx, line in enumerate(content):
    p, v = line.split(" ")
    x, y = p.replace("p=", "").split(",")
    dx, dy = v.replace("v=", "").split(",")
    robots[idx] = {"x": int(x), "y": int(y), "dx": int(dx), "dy": int(dy)}

# Going to search for 5x5 squares that are completely filled for each second-state.
squares = [
    complex(x, y) for x in range(5) for y in range(5)
]

# Super inefficient but I am tired.
def check_for_square(locs:set[complex]):
    for y in range(len_y-4):
        for x in range(len_x-4):
            to_check = set([complex(x,y) + s for s in squares])
            if locs.issuperset(to_check):
                return True
    return False
            

for i in range(1, 10000):
    locs = set()

    for robot, f in robots.items():
        new_x = (f["x"] + i * f["dx"]) % len_x
        new_y = (f["y"] + i * f["dy"]) % len_y
        locs.add(complex(new_x, new_y))
    if i % 50 == 0:
        print(i)
    if check_for_square(locs):
        with open(f"./day14/prints/{i}.txt", "w") as f:
            for y in range(len_y):
                row = ""
                for x in range(len_x):
                    if complex(x,y) in locs:
                        row += "X"
                    else:
                        row += " "
                f.write(row+"\n")


result = 0

print(f"Part 2: {result}, {elapsed(start_time)}")
print("Check folder 'prints'...")