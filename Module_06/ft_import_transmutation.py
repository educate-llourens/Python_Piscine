#!/usr/bin/env python3

import alchemy.elements
from alchemy.elements import create_fire, create_earth
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion


def main() -> None:
    # Variables ***************************************************************

    # Methods of import *******************************************************
    print("=== Import Transmutation Mastery ===\n")

    # Full module import --------------------------------------------
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire():", end=" ")
    try:
        print(f"{alchemy.elements.create_fire()}\n")
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Specific function import --------------------------------------
    print("Method 2 - Specific function import:")
    print("create_water():", end=" ")
    try:
        print(f"{create_water()}\n")
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Aliased import ------------------------------------------------
    print("Method 3 - Aliased import:")
    print("heal():", end=" ")
    try:
        print(f"{heal()}\n")
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Multiple imports ----------------------------------------------
    print("Method 4 - Multiple imports:")
    try:
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strength_potion()}\n")
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Final message -------------------------------------------------
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
