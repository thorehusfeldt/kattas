#!/usr/bin/env python3

s = input()
l = list(s)
bit = '0'
for i in range(len(l)):
    if l[i] == 'b':
        l[i] = bit
        if bit == '0':
            bit = '1'
        else:
            bit = '0'
print(''.join(l))
