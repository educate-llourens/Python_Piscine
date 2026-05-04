#!/usr/bin/env python3

from functools import reduce, partial
from operator import add, mul
from typing import List
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda x, y: add(x, y), spells)
    elif operation == "multiply":
        return reduce(lambda x, y: mul(x, y), spells)
    elif operation == "max":
        return reduce(lambda x, y: max(x, y), spells)
    elif operation == "min":
        return reduce(lambda x, y: min(x, y), spells)
    return 0


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} dealt {power} points of {element} damage"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantment: Callable

    enchantment = partial(base_enchantment, 50, "Fire")
    return {"fire_enchanter": enchantment}


def main() -> None:
    # Variables ***************************************************************
    reducer_list: List[int]

    # Testing Spell Reducer ***************************************************
    reducer_list = [10, 10, 50, 30]
    print(f"Sum: {spell_reducer(reducer_list, "add")}")
    print(f"Product: {spell_reducer(reducer_list, "multiply")}")
    print(f"Max: {spell_reducer(reducer_list, "max")}")
    print(f"Min: {spell_reducer(reducer_list, "min")}\n")

    # Testing Partial Enchanter ***********************************************
    


if __name__ == "__main__":
    main()
