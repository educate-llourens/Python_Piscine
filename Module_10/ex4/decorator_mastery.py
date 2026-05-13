#!/usr/bin/env python3

from functools import wraps
from typing import Any
from time import perf_counter
from collections.abc import Callable


def spell_timer(function: Callable) -> Callable:
    @wraps(function)
    def wrapped_function(*pos_args, **key_word_args) -> Callable:
        start_timer: float
        end_timer: float
        result: Any

        print(f"Casting {function.__name__}...")
        start_timer = perf_counter()
        result = function(*pos_args, **key_word_args)
        end_timer = perf_counter()
        # Change to 7 decimal places to see result
        print(f"Spell completed in {end_timer - start_timer:.3f} seconds")
        return result
    return wrapped_function


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable:
    def validate_power(function: Callable) -> Callable:
        @wraps(function)
        def wrapped_function(*pos_args, **key_word_args) -> Any:
            if pos_args and pos_args[2] >= min_power:
                return function(*pos_args, **key_word_args)
            return "Insufficient power for this spell"
        return wrapped_function
    return validate_power


def retry_spell(max_attempts: int) -> Callable:
    def retry(function: Callable) -> Callable:
        @wraps(function)
        def wrapped_function(*pos_args, **key_word_args) -> Any:
            retry_counter: int = 0

            while retry_counter < max_attempts:
                try:
                    return function(*pos_args, **key_word_args)
                except Exception:
                    retry_counter += 1
                    if retry_counter == max_attempts:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts")
                    else:
                        print("Spell failed, retrying... (attempt "
                              f"{retry_counter}/{max_attempts})")
        return wrapped_function
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for item in name:
                if not item.isalpha() and item != " ":
                    return False
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@retry_spell(3)
def victim_scream(hit_successful: bool) -> str:
    if not hit_successful:
        raise ValueError("Hit missed")
    return "Waaaaaaagh spelled !"


@power_validator(10)
def enough_power(spell_name: str, damage_type: str, power: int) -> str:
    return f"{spell_name} dealt {damage_type} damage for {power} points"


def main() -> None:
    # Variables ***************************************************************
    guild = MageGuild()

    # Testing Spell Timer *****************************************************
    print("Testing spell timer...")
    print(fireball())
    print("")

    # Testing Retrying spell **************************************************
    print("Testing retrying spell...")
    print(victim_scream(False))
    print(victim_scream(True))
    print("")

    # Testing MageGuild class *************************************************
    print("Testing MageGuild...")
    print(guild.validate_mage_name("This will pass"))
    print(guild.validate_mage_name("This_will_fail"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 5))


if __name__ == "__main__":
    main()
