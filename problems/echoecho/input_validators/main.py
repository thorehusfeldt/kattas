#!/usr/bin/env python3

import re
import sys

line = sys.stdin.readline()
if not re.match(r"(Hello|Hallo)\n", line):
    print("Hello or Hallo expected", file=sys.stderr)
    sys.exit(43)

if not sys.stdin.readline() == "":
    print("Extra input", file=sys.stderr)
    sys.exit(43)
sys.exit(42)
