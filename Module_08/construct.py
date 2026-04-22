#!/usr/bin/env python3

import sys


def print_venv_output() -> None:
    print("\nMATRIX STATUS: Welcome to the construct")


def construct() -> None:
    if sys.prefix != sys.base_prefix:
        print_venv_output()


if __name__ == "__main__":
    construct()
