#!/usr/bin/env python3

from functools import wraps
from typing import Any
from time import perf_counter
from collections.abc import Callable


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        return ""


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapped_function(*pos_args, **key_word_args) -> Callable:
        start_timer: float
        end_timer: float
        result: Any

        print(f"Casting {func.__name__}...")
        start_timer = perf_counter()
        result = func(*pos_args, **key_word_args)
        end_timer = perf_counter()
        # Change to 7 decimal places to see result
        print(f"Spell completed in {end_timer - start_timer:.3f} seconds")
        return result
    return wrapped_function


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable:
    return (spell_timer)


def retry_spell(max_attempts: int) -> Callable:
    def retry(function: Callable) -> Callable:
        retry_counter: int = 0

        @wraps
        def wrapped_function(*pos_args, **key_word_args) -> Callable:
            result: Any
            nonlocal retry_counter

            try:
                result = function(*pos_args, **key_word_args)
            except Exception:
                retry_counter += 1
            return result
        return wrapped_function
    return retry


def main() -> None:
    # Variables ***************************************************************

    # Testing Spell Timer *****************************************************
    print("Testing spell timer...")
    print(fireball())
    print("")

    # Testing Retrying spell **************************************************


if __name__ == "__main__":
    main()
