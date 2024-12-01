import os

for i in range(2, 26, 1):
    # create folder
    folder = f"./day{i:02d}"
    os.mkdir(folder)
    # create files
    for part in range(1, 3, 1):
        with open(f"{folder}/day{i:02d}-part {part}.py", "w") as f:
            f.write(f"# Advent of Code 2024 - Day {i:02d}\n")
            f.write("# Author: Jarro van Ginkel\n")
            f.write(f"# Part {part}\n")
            f.write("\n")
            f.write("# Possible imports required:\n")
            f.write("from rich import print\n")
            f.write("#import re\n")
            f.write("\n")
            f.write(f'with open("{folder}/example.txt") as f:\n')
            if part == 2:
                f.write(f'#with open("{folder}/example-2.txt") as f:\n')
            f.write(f'#with open("{folder}/input.txt") as f:\n')
            f.write('    content = f.read().split("\\n")\n')
            f.write("\n")
            f.write("\n")

    with open(folder + "/input.txt", "w") as f:
        pass
    with open(folder + "/example.txt", "w") as f:
        pass
    with open(folder + "/example-2.txt", "w") as f:
        pass