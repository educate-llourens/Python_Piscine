#!/usr/bin/env python3

from alchemy.grimoire.dark_spellbook import dark_spell_record


def kaboom_1() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(f'{dark_spell_record("Killing curse", "Spider-eye, eyeball, toad")}')


if __name__ == "__main__":
    kaboom_1()
