# Advent of Code 2024 - Day 24 - part 2
# Author: Jarro van Ginkel
from copy import deepcopy

from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from typing import Callable

wires, gates = parse_data_as_lines(24, "\n\n")
result = []

ws: dict[str, bool] = {}
gs: dict[str, tuple[str, str, Callable]] = {}
zs: list[str] = []
def _and(a, b):
    return a & b

def _or(a, b):
    return a | b

def _xor(a, b):
    return a ^ b

for wire in wires.split("\n"):
    w, v = wire.split(": ")
    ws[w] = bool(int(v))

for gate in gates.split("\n"):
    w1, opp, w2, _, out = gate.split(" ")
    if opp == "AND":
        f = _and
    elif opp == "OR":
        f = _or
    else: 
        f = _xor
    gs[out] = (w1, w2, f)

    if out.startswith("z"):
        zs.append(out)

zs.sort(reverse=True)

def calc(wire: str, wires: dict[str, bool] = ws, gates: dict[str, tuple[str, str, Callable]] = gs):
    if wire in wires:
        return wires[wire]
    r = gates[wire][2](calc(gates[wire][0]), calc(gates[wire][1]))
    wires[wire] = r
    return r

# All x and y numbers are provided, so we can calculate what the outcome of z's should have been.
# compare with current z's outcome, and determine what needs to be swapped? would it be that easy?
# Inspection: both x and y are the same number in decimal. 
# So, z should be bit-shifted 1 (left) of either y or x. Current z is already 1 bit longer. 
# 
ys = []
xs = []

for wire in ws.keys():
    if wire.startswith("y"):
        ys.append(wire)
    elif wire.startswith("x"):
        xs.append(wire)
ys.sort(reverse=True)
xs.sort(reverse=True)

y_bits = [int(ws[y]) for y in ys]
x_bits = [int(ws[y]) for y in ys]
# y_val = int("".join([str(y) for y in y_bits]), 2)
# x_val = int("".join([str(x) for x in x_bits]), 2)
# print(y_val, x_val)
# print(f"y bits: {y_bits}")
# print(f"x bits: {x_bits}")

z_should = deepcopy(y_bits)
z_should.append(0)

# we know current z from part 1:
z_is = []
for z in zs:
    r = calc(z)
    z_is.append(int(r))

assert len(z_is) == len(z_should)

# tuple: z, index, z_is, z_should
z_miss: list[tuple[str, int, int, int]] = []
for i, (zis, zshould) in enumerate(zip(z_is, z_should)):
    if zis != zshould:
        print(f"{i}: is {zis} should {zshould}")
        # print(zs[i], gs[zs[i]][0], gs[zs[i]][1])
        z_miss.append((zs[i], i, zis, z_should))

# Now we have a list of z's which output should be different, in my input it's 23 long. 
# There should be 8 gates that influence these z's. If the z's are direct opp(x,y), they must be 
# switched. 
# Update: there are no direct opp(x,y) in these 23 z's. In fact, all operands to these z's 
# are unique (46 in total). 
# XOR and AND operators are sure to switch value if one of the operands change, OR could remain the same. 
# Let's filter for operators then?

 
# ors = []
# xors = []
# ands = []
# for z, i, zis, zshould in z_miss:
#     if gs[z][2] == _or:
#         ors.append(z)
#     elif gs[z][2] == _xor:
#         xors.append(z)
#     else:
#         ands.append(z)

# print("xor: ", xors)
# print("and: ", ands)
# print("ors: ", ors)

# There are 21 XORs, 1 AND and 1 OR. Is that significant? 
# maybe if we manually add each gate to the ws dict, and recalc, we can see 
# what the impact is on the outcome (e.g. the list of bits of z's). 
result = 0

print(f"Part 2: {result}, {elapsed(start_time)}")