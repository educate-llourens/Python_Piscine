#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argv_len: int = len(sys.argv)
    i: int = 0

    if argv_len > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argv_len - 1}")
        for i in range(1, argv_len):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {argv_len}")
    else:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {argv_len}")
