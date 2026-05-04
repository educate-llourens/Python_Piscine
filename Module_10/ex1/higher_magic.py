#!/usr/bin/env python3

from collections.abc import Callable
from typing import Tuple, List, Any


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combine_spells(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combine_spells


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def increase_spell(target: str, power: int) -> str:
        return (base_spell(target, power * 3))
    return increase_spell


def conditional_caster(
    condition: Callable[..., Any],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def condition_for_spell(target: str, power: int) -> str:
        if condition(target, power):
            return (spell(target, power))
        else:
            return "Spell fizzled"
    return condition_for_spell


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], List[str]]:
    def call_all_spells(target: str, power: int) -> List[str]:
        result_list: List[str] = []

        for spell in spells:
            result_list.append(spell(target, power))
        return result_list
    return call_all_spells


def spell_condition(target: str, power: int) -> bool:
    if power > 45:
        return True
    return False


def main() -> None:
    # Variables ***************************************************************
    smushed_spells: Callable[[str, int], tuple[str, str]]
    result_str_1: str
    result_str_2: str
    amplified_power: Callable[[str, int], str]
    power_str: str
    condition_met: Callable[[str, int], str]
    valid_condition: str
    invalid_condition: str
    spells_list: List[Callable[[str, int], str]]
    call_spells: Callable[[str, int], List[str]]
    list_spells: List[str]

    # Test Spell Combiner *****************************************************
    print("Testing spell combiner...")
    smushed_spells = spell_combiner(fireball, heal)
    result_str_1, result_str_2 = smushed_spells("Dragon", 45)
    print(f"{result_str_1}, {result_str_2}\n")

    # Test Power Amplifier ****************************************************
    print("Testing Power amplifier...")
    amplified_power = power_amplifier(heal, 10)
    power_str = amplified_power("Snuzzler3000", 10)
    print(f"Original: 10 HP, Amplified: {power_str.split("for ")[1]}\n")

    # Test Conditional Caster *************************************************
    print("Testing Conditional Caster with valid condition. Condition: "
          "Power must be more than 50 to cast successfully")
    condition_met = conditional_caster(spell_condition, fireball)
    valid_condition = condition_met("Orc", 55)
    print("Power = 50:")
    print(f"{valid_condition}\n")
    print("Testing Conditional Caster with invalid condition. Condition: "
          "Power must be more than 50 to cast successfully")
    invalid_condition = condition_met("Siren", 15)
    print("Power: 15")
    print(f"{invalid_condition}\n")

    # Test spell sequence *****************************************************
    print("Testing Spell sequence...")
    spells_list = [fireball, heal]
    call_spells = spell_sequence(spells_list)
    list_spells = call_spells("Minotour", 150)
    for spell in list_spells:
        print(f"{spell}")


if __name__ == "__main__":
    main()
