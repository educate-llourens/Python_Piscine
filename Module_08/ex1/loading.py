#!/usr/bin/env python3

import importlib.util
from typing import List

def loading() -> None:
    required_libraries: List[str] = ["pandas", "numpy", "matplotlib"]

    print("LOADING STATUS: Loading programs...")
    for library in required_libraries:
        if importlib.util.find_spec(library) is None:
            print(f"Missing library {library}. Install with one of the below:")
            print(f"   1. pip install {library}")
            print(f"   2. poetry install {library}")
        else:
            module = importlib.import_module(library)
            version = getattr(module, '__version__', None)
            print(f"[OK] {library} ({version}) - ", end="")
            if library == "pandas":
                print("Data manipulation ready")
            elif library == "numpy":
                print("Numerical computation ready")
            elif library == "matplotlib":
                print("Visualization ready")
    print("")

    print("Analyzing Matrix data...")


if __name__ == "__main__":
    loading()