#!/usr/bin/env python3
import sys
from collections import defaultdict

current_key = None
a_values = defaultdict(int)
b_values = defaultdict(int)

for line in sys.stdin:
    key, value = line.strip().split("\t")
    i, j = map(int, key.strip().split(","))
    tag, k, val = value.strip().split(",")
    k = int(k)
    val = int(val)

    if current_key != (i, j):
       
        if current_key:
            total = 0
            for index in a_values:
                total += a_values[index] * b_values.get(index, 0)
            print(f"{current_key[0]},{current_key[1]}\t{total}")
       
        current_key = (i, j)
        a_values = defaultdict(int)
        b_values = defaultdict(int)

    if tag == "A":
        a_values[k] = val
    elif tag == "B":
        b_values[k] = val


if current_key:
    total = 0
    for index in a_values:
        total += a_values[index] * b_values.get(index, 0)
    print(f"{current_key[0]},{current_key[1]}\t{total}")

