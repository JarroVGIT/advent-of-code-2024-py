import os

for i in range(10, 26, 1):
    # create folder
    folder = f"./day{i:02d}"
    os.mkdir(folder)
    # create files
    for part in range(1, 3, 1):
        with open(f"{folder}/day{i:02d}-part {part}.py", "w") as f:
            f.write(f"# Advent of Code 2024 - Day {i:02d} - part {part}\n")
            f.write("# Author: Jarro van Ginkel\n")
            f.write("from rich import print\n")
            f.write("import time\n")
            f.write("\n")
            f.write(f'with open("{folder}/example.txt") as f:\n')
            f.write(f'#with open("{folder}/input.txt") as f:\n')
            f.write('    content = f.read().split("\\n")\n')
            f.write("\n")
            f.write("def elapsed(start_time):\n")
            f.write("    elapsed = time.time() - start_time\n")
            f.write("    minutes = int(elapsed // 60)\n")
            f.write("    seconds = int(elapsed % 60)\n")
            f.write("    milliseconds = int((elapsed % 1) * 1000)\n")
            f.write("    return f\"{minutes:02}:{seconds:02}:{milliseconds:03}\"\n")
            f.write("start_time = time.time()\n")
            f.write("\n\n\n\n")
            f.write("result = 0\n")
            f.write("\n")
            f.write(f"print(f\"Part {part}: {{result}}, {{elapsed(start_time)}}\")")

    with open(folder + "/input.txt", "w") as f:
        pass
    with open(folder + "/example.txt", "w") as f:
        pass