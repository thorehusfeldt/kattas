#!/usr/bin/env python3
"""Constraints checking for BAPCtools """

import sys

constraints_file = None
if "--constraints_file" in sys.argv:
    constraints_file = sys.argv[sys.argv.index("--constraints_file") + 1]

def fail(message):
    """Reject this testcase with the given message"""
    print(message, file=sys.stderr)
    sys.exit(43)


def integer(var, lo, hi, name, message=None):
    """Validate (and write to constraints file) that lo <= var <= hi"""

    if constraints_file is not None:
        with open(constraints_file, "a") as file:
            print(
                f"{name} {name} {int(var == lo)} {int(var == hi)} {var} {var} {lo} {hi}",
                file=file,
            )
    if not lo <= var <= hi:
        fail(message or f"{name} out of range, expected {lo} <= {var} <= {hi}")
