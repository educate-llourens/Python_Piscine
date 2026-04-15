#!/usr/bin/env python3

from alchemy.grimoire.light_spellbook import light_spell_record


def kaboom_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f'Testing record light spell: '
          f'{light_spell_record("Fantasy", "Earth, wind and fire")}')


if __name__ == "__main__":
    kaboom_0()
