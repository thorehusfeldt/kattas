#!/usr/bin/env python3

import random
from argparse import ArgumentParser

parser = ArgumentParser(description='Generate random instance')

parser.add_argument('-n', type=int)
parser.add_argument('--prob_b', '-p', type=float, default=1/2)
parser.add_argument('--seed', type=int)
args = parser.parse_args()

random.seed(args.seed)

line: list[str] = []
for _ in range(args.n):
    letter = 'b' if random.random() <= args.prob_b else 'a'
    line.append(letter)

assert len(line) == args.n
print(*line, sep='')
