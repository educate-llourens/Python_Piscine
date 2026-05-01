#!/usr/bin/env python3

from collections.abc import Callable
from typing import Tuple, List


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine_spells(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combine_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def increase_spell(target: str, power: int) -> str:
        return (base_spell(base_spell(target, power * 3)))
    return increase_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condition_for_spell(target: str, power: int) -> str:
        if condition:
            return (spell(target, power))
        else:
            return "Spell fizzled"
    return condition_for_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    for spell in spells:
        def call_spell(target:str, power: int) -> str:
            return (spell(target, power))
    return call_spell
