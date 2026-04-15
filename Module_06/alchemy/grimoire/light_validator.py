#!/usr/bin/env python3

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    is_valid: bool = False

    for element in allowed_ingredients:
        if element in ingredients:
            is_valid = True
    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
