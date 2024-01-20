#!/usr/bin/env python3

import re
import sys
import validation


line = sys.stdin.readline()
if not re.match(r"(0|[1-9][0-9]*\n)", line):
    validation.fail("Integer expected")

x = int(line)
validation.integer(x, -10, 10, "c")

if not sys.stdin.readline() == "":
    validation.fail("Extra input")
sys.exit(42)
