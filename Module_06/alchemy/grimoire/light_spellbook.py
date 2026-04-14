#!/usr/bin/env python3

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    valid_return_str: str = f"Spell recorded: {spell_name} ("
    valid_elements: list[str] = []
    i: int = 0

    for element in light_spell_allowed_ingredients():
        if element in ingredients:
            valid_elements.append(element)
    if valid_elements:
        for i in range(len(valid_elements)):
            if i == 0:
                valid_return_str += valid_elements[i].capitalize()
            elif i == len(valid_elements):
                valid_return_str += "and"
                valid_return_str += valid_elements[i]
            else:
                valid_return_str += ", "
                valid_return_str += valid_elements[i]
        valid_return_str += " - VALID)"
        return valid_return_str
    return "Ingredients INVALID"
