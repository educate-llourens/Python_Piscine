#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    nbr_calls: int = 0

    def count_calls() -> int:
        nonlocal nbr_calls

        nbr_calls += 1
        return nbr_calls
    return count_calls


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power: int = initial_power

    def increase_power(add_power: int) -> int:
        nonlocal total_power

        total_power += add_power
        return total_power
    return increase_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def add_enchantment(item: str) -> str:
        return (f"{enchantment_type} {item}")
    return add_enchantment


def memory_vault() -> dict[str, Callable]:
    vault: dict = {}

    def store(key: str, value: Any):
        vault[key] = value

    def recall(key: str) -> Any:
        return (vault.get(key))

    vault = {
        'store': store,
        'recall': recall
    }
    return vault


def main() -> None:
    # Variables ***************************************************************
    counter_a: Callable[[], int]
    counter_b: Callable[[], int]
    accumulated_power: Callable[[int], int]
    enchantment: Callable[[str], str]
    vault: dict

    # Testing mage counter, 3 iterations **************************************
    print("Testing mage counter...")
    counter_a = mage_counter()
    for i in range(1, 3):
        print(f"counter_a call {i}: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}\n")

    # Testing spell accumulator, 2 iterations *********************************
    print("Testing spell accumulator...")
    accumulated_power = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulated_power(20)}")
    print(f"Base 100, add 30: {accumulated_power(30)}\n")

    # Testing enchantment factory, two enchantments ***************************
    print("Testing enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    enchantment = enchantment_factory("Frozen")
    print(enchantment("Shield\n"))

    # Testing memory vault ****************************************************
    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']("secret", 42)
    print("Store 'secret' = 42")
    vault['recall']("secret")
    print(f"Recall 'secret': {vault['secret']}")
    try:
        print(f"Recall 'unknown': {vault['unknown']}")
    except KeyError:
        print("Recall 'unknown': Memory not found")


if __name__ == "__main__":
    main()
