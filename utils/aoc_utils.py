import time
import sys
from rich import print

start_time = time.time()

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

def parse_data_as_lines(day: int, sep="\n") -> list[str]:
    if "--example" in sys.argv:
        file_path = f"./day{day:02}/example.txt" 
    else: 
        file_path = f"./day{day:02}/input.txt"
    with open(file_path) as f:
        content = f.read().split(sep)
    return content

def parse_data_as_grid(day: int) -> dict[complex, str]:
    content = parse_data_as_lines(day)
    grid = {}
    for y, row in enumerate(content):
        for x, val in enumerate(row):
            grid[complex(x,y)] = val
    return grid

def print_grid(grid:dict[complex, str], missing_val=".") -> None:
    min_y = int(min(c.imag for c in grid.keys()))
    min_x = int(min(c.real for c in grid.keys()))
    max_y = int(max(c.imag for c in grid.keys()))
    max_x = int(max(c.real for c in grid.keys()))

    for y in range(min_y, max_y+1):
        row = ""
        for x in range(min_x, max_x+1):
            row += grid.get(complex(x,y), missing_val)
        print(row)
