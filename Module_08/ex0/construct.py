#!/usr/bin/env python3

import sys
import os
import site


# Inside the venv *************************************************************
def print_venv_output() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.prefix}")
    print(f"Virtual environment: {os.path.basename(sys.prefix)}")
    print(f"Environment path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment! "
          "Safe to install packages without affecting"
          "the global system.\n")

    print(f"Package installation path: \n{site.getsitepackages()[0]}")


# No venv *********************************************************************
def print_global_output() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.prefix}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment! "
          "The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")

    print("Then run this program again.")


def construct() -> None:
    if sys.prefix != sys.base_prefix:
        print_venv_output()
    else:
        print_global_output()


if __name__ == "__main__":
    construct()
