#!/usr/bin/env python3

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    result: str = ""

    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"
