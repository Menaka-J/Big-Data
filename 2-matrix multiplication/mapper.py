#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) != 4:
        continue
    matrix, i, j, value = parts
    i, j, value = int(i), int(j), int(value)

    if matrix == "A":
        for col in range(2):   
            print(f"{i},{col}\tA,{j},{value}")
    elif matrix == "B":
        for row in range(2):  
            print(f"{row},{j}\tB,{i},{value}")
