#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        """
        Args:
            name (str): Creature's name
            creature_type (str): Typing of the creature
        """

    @abstractmethod
    def attack(self) -> str:
        """
        Returns:
            str: Returns attack with name and type
        """
        return ""

    def describe(self) -> str:
        return ""


class Flameling(Creature):
    """Base flame creature
    """
    def __init__(self) -> None:
        self.name = "Flameling"
        self.creature_type = "Fire"

    def attack(self) -> str:
        """
        Returns:
            str: Flameling specific attack string
        """
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """Evolution of Flameling
    """
    def __init__(self) -> None:
        self.name = Pyrodon
        self.creature_type = "Fire/Flying"

    def attack(self) -> str:
        """
        Returns:
            str: Pyrodon specific attack string
        """
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """Base water creature
    """
    def __init__(self) -> None:
        self.name = Aquabub
        self.creature_type = "Water"

    def attack(self) -> str:
        """
        Returns:
            str: Aquabub specific attack string
        """
        return f"{self.name} uses watergun!"


class Torragon(Creature):
    """Evolution of Aquabub
    """
    def __init__(self) -> None:
        self.name = Torragon
        self.creature_type = "Water"

    def attack(self) -> str:
        """
        Returns:
            str: Torragon specific attack string
        """
        return f"{self.name} uses Hydro Pump!"
