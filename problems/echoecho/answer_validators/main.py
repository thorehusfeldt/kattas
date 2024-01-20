#!/usr/bin/env python3

import sys

l = len(sys.stdin.readlines())
if not  l == 2:
    print("Expected 2 lines, got {l}", file=sys.stderr)
    sys.exit(43)
sys.exit(42)
