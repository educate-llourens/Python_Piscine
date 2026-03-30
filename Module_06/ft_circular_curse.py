#!/usr/bin/env python3

def main() -> None:
    print("=== Circular Curse Breaking ===\n")

    # Ingredient validation ***************************************************
    print("Testing ingredient validation:")
    try:
        print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
    except AttributeError:
        print("AttributeError: import not correct\n")

if __name__ == "__main__":
    main()
