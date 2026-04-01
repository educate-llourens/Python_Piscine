#!/usr/bin/env python3

from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:
    print("=== Circular Curse Breaking ===\n")

    # Ingredient validation ***************************************************
    print("Testing ingredient validation:")
    try:
        print(f'validate_ingredients("fire air"): '
              f'{validate_ingredients("fire air")}')
        print('validate_ingredients("dragon scales"): '
              f'{validate_ingredients("dragon scales")}\n')
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Spell recording with validation *****************************************
    print("Testing spell recording with validation:")
    try:
        print('record_spell("Fireball", "fire air"): '
              f'{record_spell("Fireball", "fire air")}')
        print('record_spell("Dark Magic", "shadow"): '
              f'{record_spell("Dark Magic", "shadow")}\n')
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Testing late import *****************************************************
    print("Testing late import technique:")
    try:
        print('record_spell("Lightning", "air"): '
              f'{record_spell("Lightning", "air")}\n')
    except AttributeError:
        print("AttributeError: import not correct\n")

    # Final message ***********************************************************
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
