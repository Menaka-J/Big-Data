#!/usr/bin/env python3
import sys

for line in sys.stdin:
line=line.strip()
words=line.split()
for i in words:
print(f"{i}\t1")
