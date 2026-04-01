#!/usr/bin/env python3

from alchemy.transmutation import (lead_to_gold, stone_to_gem,
                                   philosophers_stone, elixir_of_life)
import alchemy


def main() -> None:
    print("=== Pathway Debate Mastery ===\n")

    # Absolute imports ********************************************************
    print("Testing Absolute Imports (from basic.py):")
    try:
        print(f"lead_to_gold(): {lead_to_gold()}")
        print(f"stone_to_gem(): {stone_to_gem()}\n")
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Relative imports from advanced.py ***************************************
    print("Testing Relative Imports (from advanced.py):")
    try:
        print(f"philosophers_stone(): {philosophers_stone()}")
        print(f"elixir_of_life(): {elixir_of_life()}\n")
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Package access **********************************************************
    print("Testing Package Access:")
    try:
        print("alchemy.transmutation.lead_to_gold(): "
              f"{alchemy.transmutation.lead_to_gold()}")
        print("alchemy.transmutation.philosophers_stone(): "
              f"{alchemy.transmutation.philosophers_stone()}\n")
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Final message ***********************************************************
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
