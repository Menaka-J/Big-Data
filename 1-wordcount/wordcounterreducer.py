#!/usr/bin/env python3
import sys

cword=None
ccount=0

for line in sys.stdin:
word,count=line.strip().split('\t')
count=int(count)

if word==cword:
ccount+=count
else:
if cword:
print(f"{cword}\t{ccount}")
cword=word
ccount=count

if cword:
print(f"{cword}\t{ccount}")
