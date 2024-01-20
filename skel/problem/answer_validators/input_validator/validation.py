#!/usr/bin/env python3
"""Constraints checking for BAPCtools """

import sys
from argparse import ArgumentParser

parser = ArgumentParser(description="Accept constraints_file from BAPCtools")
parser.add_argument("input", type=str)
parser.add_argument("--constraints_file", type=str)
args = parser.parse_args()


def fail(message):
    """Reject this testcase with the given message"""
    print(message, file=sys.stderr)
    sys.exit(43)


def integer(var, lo, hi, name, message=None):
    """Validate (and write to constraints file) that lo <= var <= hi"""

    if args.constraints_file:
        with open(args.constraints_file, "a") as file:
            print(
                f"{name} {name} {int(var == lo)} {int(var == hi)} {var} {var} {lo} {hi}",
                file=file,
            )
    if not lo <= var <= hi:
        fail(message or f"{name} out of range, expected {lo} <= {var} <= {hi}")
