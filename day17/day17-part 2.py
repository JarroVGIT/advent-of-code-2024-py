# Advent of Code 2024 - Day 17 - part 2
# Author: Jarro van Ginkel
from rich import print
import time
from functools import lru_cache
from functools import reduce
from copy import copy

# with open("./day17/example.txt") as f:
# with open("./day17/example2.txt") as f:
with open("./day17/input.txt") as f:
    registers, program = f.read().split("\n\n")

def elapsed(start_time):
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed % 1) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
start_time = time.time()

def reset_reg(multiplier: int) -> dict[str, int]:
    reg = {}
    for line_idx, r in enumerate(["A", "B", "C"]):
        val = int(registers.split("\n")[line_idx].split(": ")[-1])
        reg[r] = val
    reg["A"] *= multiplier
    return reg

program = [int(i) for i in program.split(": ")[-1].split(",")]


def get_combo_val(reg: dict[str, int], operand: int) -> int:
    if operand < 4:
        return operand
    else:
        return reg.get(["A", "B", "C"][operand-4])

def run_program(reg: dict[str, int]) -> list[str]:
    instruction_ptr = 0
    output = []
    while instruction_ptr < len(program):
        opcode = program[instruction_ptr]
        operand = program[instruction_ptr+1]

        if opcode == 0:
            num = reg["A"]
            denom = 2**get_combo_val(reg, operand)
            reg["A"] = int(num/denom)
            instruction_ptr += 2
        
        elif opcode == 1:
            reg["B"] = reg["B"] ^ operand
            instruction_ptr += 2
        
        elif opcode == 2:
            reg["B"] = get_combo_val(reg, operand) % 8
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
            output.append(get_combo_val(reg, operand)%8)
            instruction_ptr += 2
        
        elif opcode == 6:
            num = reg["A"]
            denom = 2**get_combo_val(reg, operand)
            reg["B"] = int(num/denom)
            instruction_ptr += 2

        elif opcode == 7:
            num = reg["A"]
            denom = 2**get_combo_val(reg, operand)
            reg["C"] = int(num/denom)
            instruction_ptr += 2
    return output

# Program only adjusts A in one step (opcode 0)
# operand in that step is 3, so denom is always 2**3=8.
# Only when A//8 == 0, the program exits (last opcode in program)
# Each iteration, there is only one output (opcode 5) call.
# In the last iteration, A must be 1-7, so second last iteration, 
# A must be between 8 times that + 7. 
# Example: last_iteration: A = 7 (will result in A=0)
# second last iteration must be between 7*8 (56) to 7*8+7 (63), 
# because every int between 56 and 63 floor-divided by 8 = 7. 
# For each of that possibility, you again have 8 possbile numbers
# preceding. Each iteration will yield an output, which we can match
# against the last numbers of the program. I have checked by hand that
# if A is set to 1, the output is the same as program[-1]. I created a BFS
# which takes a list of 0-7 values, and calculates the A based on that.
# This is reducing (acc * 8 + i) where acc starts at 0. It returns a list
# of lists of ints, all of them resulting building up to the program output.
# Then finally, calculate the minimum A for the resulting lists of ints.


def get_next_iteration(lists_so_far: list[list[int]]) -> list[list[int]]:
    result = []
    for lst in lists_so_far:
        for i in range(0,8):
            p = copy(lst)
            p.append(i)
            a = reduce(lambda acc, val: (acc * 8) + val, p, 0)
            reg = {"A": a, "B": 0, "C": 0}
            r = run_program(reg)
            if program[(-len(p)):]==r[(-len(p)):]:
                result.append(p)
    return result

solutions: list[list[int]] = [[1]]
for i in range(1, len(program)):
    solutions = get_next_iteration(solutions)

# Get lowest possible A from solutions list.

result = reduce(lambda acc, val: (acc * 8) + val, solutions[0], 0)
for solution in solutions[1:]:
    s = reduce(lambda acc, val: (acc * 8) + val, solution, 0)
    result = min(result, s)

print(f"Part 2: {result}, {elapsed(start_time)}")