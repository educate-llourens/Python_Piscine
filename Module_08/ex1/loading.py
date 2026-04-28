#!/usr/bin/env python3

import importlib.util
from numpy import random
from pandas import DataFrame
from matplotlib import pyplot
from typing import List


def handle_data() -> None:
    data: List[int] = []
    spreadsheet: DataFrame = object()

    print("Analyzing Matrix data...")
    data = random.normal(size=1000)

    print("Processing 1000 data points...")
    spreadsheet = DataFrame({'Generated numbers': data})

    print("Generating visualization...\n")
    pyplot.figure(figsize=(10, 10))
    pyplot.scatter(spreadsheet.index, spreadsheet["Generated numbers"])
    pyplot.title('Random 1000 numbers graph')
    pyplot.xlabel("Amount of numbers generated")
    pyplot.ylabel("Number range")
    pyplot.grid(True, color='violet', alpha=0.3)
    pyplot.savefig('matrix_analysis.png', dpi=300)
    pyplot.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def loading() -> None:
    # Variables ***************************************************************
    required_libraries: List[str] = ["pandas", "numpy", "matplotlib"]

    # Checking libraries exist ************************************************
    print("LOADING STATUS: Loading programs...")
    for library in required_libraries:
        if importlib.util.find_spec(library) is None:
            print(f"Missing library {library}. Install with one of the below:")
            print(f"   1. pip install {library}")
            print(f"   2. poetry install {library}")
            print("")
            return
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
                handle_data()


if __name__ == "__main__":
    loading()
