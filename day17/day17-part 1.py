# Advent of Code 2024 - Day 17 - part 1
# Author: Jarro van Ginkel
from rich import print
import time

#with open("./day17/example.txt") as f:
with open("./day17/input.txt") as f:
    registers, program = f.read().split("\n\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

reg = {}
for line_idx, r in enumerate(["A", "B", "C"]):
    val = int(registers.split("\n")[line_idx].split(": ")[-1])
    reg[r] = val

program = [int(i) for i in program.split(": ")[-1].split(",")]


def get_combo_val(operand: int) -> int:
    if operand < 4:
        return operand
    else:
        return reg.get(["A", "B", "C"][operand-4])

instruction_ptr = 0
output = []
while instruction_ptr < len(program):
    opcode = program[instruction_ptr]
    operand = program[instruction_ptr+1]

    if opcode == 0:
        num = reg["A"]
        denom = 2**get_combo_val(operand)
        reg["A"] = int(num/denom)
        instruction_ptr += 2
    
    elif opcode == 1:
        reg["B"] = reg["B"] ^ operand
        instruction_ptr += 2
    
    elif opcode == 2:
        reg["B"] = get_combo_val(operand) % 8
        instruction_ptr += 2
    
    elif opcode == 3:
        if reg["A"] == 0:
            instruction_ptr += 2
        else:
            instruction_ptr = operand
    
    elif opcode == 4:
        reg["B"] = reg["B"] ^ reg["C"]
        instruction_ptr += 2
    
    elif opcode == 5:
        output.append(str(get_combo_val(operand)%8))
        instruction_ptr += 2
    
    elif opcode == 6:
        num = reg["A"]
        denom = 2**get_combo_val(operand)
        reg["B"] = int(num/denom)
        instruction_ptr += 2

    elif opcode == 7:
        num = reg["A"]
        denom = 2**get_combo_val(operand)
        reg["C"] = int(num/denom)
        instruction_ptr += 2

result = ",".join(output)

print(f"Part 1: {result}, {elapsed(start_time)}")