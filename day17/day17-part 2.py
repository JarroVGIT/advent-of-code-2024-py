# Advent of Code 2024 - Day 17 - part 2
# Author: Jarro van Ginkel
from rich import print
import time
from functools import lru_cache
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
# Only when A//9 == 0, the program exits (last opcode in program)
# Each iteration, there is only one output (opcode 5) call.
# In the last iteration, A must be 1-7, so second last iteration, 
# A must be between 8 times that + 7. 
# Example: last_iteration: A = 7 (will result in A=0)
# second last iteration must be 7*8 (56) to 7*8+7 (63), 
# because every int between 56 and 63 //8 = 7. 
# for each of that possibility, you again have 8 possbile numbers
# preceding. But all in all, a lot less than brute forcing.
# Update: well that is as worse as bruteforcing, resulting in 
# billions of numbers. New approach: see what number will result in
# the last int of the program, then try the 8 next values (*8+0 to *8+7)
# Initialize the base numbers (1 to 7) at the 9th division

# manual:
# round 1: +1
# round 2: +0
# round 3: +3 and +6
#   4 (3): +5
    
    
for i in range(0,8):
    a = ((((((1*8)+0)*8)+3)*8)+5)*8+i
    reg = {"A": a, "B": 0, "C": 0}
    print(i, program[-5:]==run_program(reg)[-5:])

for i in range(len(program)-1, 0, -1):
    

# for i in range(1, 9):
#     a = i*(8**(len(program)-1))
#     reg = {"A": a, "B": 0, "C": 0}
#     o = run_program(reg)
#     print(o)
#     print(program)
#     if 0 == program:
#         result = a


# while True:
#     reg = reset_reg(multiplier)
#     output = run_program(reg)
#     if len(output) < len(program):
#         multiplier += 1
#     else:
#         bf_a = reset_reg(multiplier-1)["A"]
#         break

# while True:
#     reg = {"A": bf_a, "B": 0, "C": 0}
#     if run_program(reg) == program:
#         result = bf_a
#         break
#     else:
#         bf_a += 1
result = 0
print(f"Part 2: {result}, {elapsed(start_time)}")