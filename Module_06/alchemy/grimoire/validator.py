#!/usr/bin/env python3

from typing import List


def validate_ingredients(ingredients: str) -> str:
    elements: List[str] = ["fire", "water", "earth", "air"]
    for item in elements:
        if item in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
