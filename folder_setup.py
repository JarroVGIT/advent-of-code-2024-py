import os

for i in range(20, 26, 1):
    # create folder
    folder = f"./day{i:02d}"
    os.mkdir(folder)
    # create files
    for part in range(1, 3, 1):
        with open(f"{folder}/day{i:02d}-part {part}.py", "w") as f:
            f.write(f"# Advent of Code 2024 - Day {i:02d} - part {part}\n")
            f.write("# Author: Jarro van Ginkel\n")
            f.write("from aoc_utils import elapsed, parse_data_as_lines, start_time\n")
            f.write("from rich import print\n")
            f.write("\n")
            f.write(f'content = parse_data_lines({i})\n')
            f.write("\n\n")
            f.write("result = 0\n")
            f.write("\n")
            f.write(f"print(f\"Part {part}: {{result}}, {{elapsed(start_time)}}\")")

    with open(folder + "/input.txt", "w") as f:
        pass
    with open(folder + "/example.txt", "w") as f:
        pass