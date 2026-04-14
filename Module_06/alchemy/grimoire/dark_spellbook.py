#!/usr/bin/env python3


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    from .dark_validator import validate_ingredients
    ingredients_validation_result = validate_ingredients(ingredients)

    if "INVALID" not in ingredients_validation_result:
        return (f"Spell recorded: {spell_name} "
                f"({ingredients_validation_result})")
    return (f"Spell not recorded: {spell_name} "
            f"({ingredients_validation_result})")
