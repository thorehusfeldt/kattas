#!/usr/bin/env python3

S = input()
res = ""
bit = '0'
for s in S:
    if s == 'a':
        res += 'a'
    if s == 'b':
        res += bit
        bit = '0' if bit == '1' else '1'
print(res)
