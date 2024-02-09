#!/usr/bin/env python3

import re
import sys
import validation


line = sys.stdin.readline()
if not re.match(r"[a01]+\n", line):
    validation.fail("[a01]+ expected")

l = len(line.strip())
validation.integer(l, 1, 500000, "c")

if not sys.stdin.readline() == "":
    validation.fail("Extra input")
sys.exit(42)
