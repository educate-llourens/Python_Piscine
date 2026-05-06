#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import List, Any
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
    water_enchantment: Callable
    ground_enchantment: Callable
    metal_enchantment: Callable

    water_enchantment = partial(base_enchantment, 50, "water")
    ground_enchantment = partial(base_enchantment, 50, "ground")
    metal_enchantment = partial(base_enchantment, 50, "metal")
    return {"water": water_enchantment,
            "ground": ground_enchantment,
            "metal": metal_enchantment}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch_spell(value: Any) -> str:
        return "Unknown spell type"

    @dispatch_spell.register(int)
    def dispatch_damage_spell(value: int) -> str:
        return f"Damage spell: {value}"

    @dispatch_spell.register(str)
    def dispatch_enchantment(enchantment: str) -> str:
        return f"Enchantment: {enchantment}"

    @dispatch_spell.register(list)
    def dispatch_multicast(spells_list: List) -> str:
        return f"Multi-cast: {len(spells_list)} spells"
    return dispatch_spell


def main() -> None:
    # Variables ***************************************************************
    reducer_list: List[int]
    enchantments: dict
    dispatch_spells: Callable[[int], str]

    # Testing Spell Reducer ***************************************************
    print("\nTesting spell reducer...")
    reducer_list = [10, 10, 50, 30]
    print(f"Sum: {spell_reducer(reducer_list, "add")}")
    print(f"Product: {spell_reducer(reducer_list, "multiply")}")
    print(f"Max: {spell_reducer(reducer_list, "max")}")
    print(f"Min: {spell_reducer(reducer_list, "min")}\n")

    # Testing Partial Enchanter ***********************************************
    print("Testing partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments['water']("Druid"))
    print(enchantments['ground']("Violet"))
    print(enchantments['metal']("Knight"))
    print("")

    # Testing Memoized Fibonacci **********************************************
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}", end=", ")
    print(f"Number of cache hits: {memoized_fibonacci.cache_info().hits}")
    print(f"Fib(1): {memoized_fibonacci(1)}", end=", ")
    print(f"Number of cache hits: {memoized_fibonacci.cache_info().hits}")
    print(f"Fib(10): {memoized_fibonacci(10)}", end=", ")
    print(f"Number of cache hits: {memoized_fibonacci.cache_info().hits}")
    print(f"Fib(15): {memoized_fibonacci(15)}", end=", ")
    print(f"Number of cache hits: {memoized_fibonacci.cache_info().hits}")
    print("")

    # Testing Spell Dispatcher ************************************************
    print("Testing spell dispatcher...")
    dispatch_spells = spell_dispatcher()
    print(dispatch_spells(42))
    print(dispatch_spells("fireball"))
    print(dispatch_spells([42, 36, 72]))
    print(dispatch_spells({'spell': "Try this"}))


if __name__ == "__main__":
    main()
