#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    valid_ingredients: list[str] = []
    return_str: str = ""
    i: int = 0

    for element in allowed_ingredients:
        if element in ingredients:
            valid_ingredients.append(element)
    if valid_ingredients:
        for i in range(len(valid_ingredients)):
            if i == 0:
                return_str = valid_ingredients[i].capitalize()
            elif i == len(valid_ingredients):
                return_str += "and "
                return_str += valid_ingredients[i]
            else:
                return_str += ", "
                return_str += valid_ingredients[i]
        return_str += " - VALID"
    return f"{ingredients} - INVALID"
