# Advent of Code 2024 - Day 24 - part 1
# Author: Jarro van Ginkel
from typing import Callable
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

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

for z in zs:
    r = calc(z)
    result.append(str(int(r)))

result = int("".join(result), 2)

print(f"Part 1: {result}, {elapsed(start_time)}")