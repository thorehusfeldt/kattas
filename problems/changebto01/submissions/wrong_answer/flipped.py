#!/usr/bin/env python3

s = list(input().strip())
bit = 1
for i, c in enumerate(s):
    if c == 'b':
        s[i] = str(bit)
        bit = 1 - bit
print(''.join(s))
