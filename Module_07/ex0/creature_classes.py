#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        """
        Args:
            name (str): Creature's name
            creature_type (str): Typing of the creature
        """
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """
        Returns:
            str: Returns attack with name and type
        """
        return ""

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    """Base flame creature
    """
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

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
        super().__init__("Pyrodon", "Fire/Flying")

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
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """
        Returns:
            str: Aquabub specific attack string
        """
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """Evolution of Aquabub
    """
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """
        Returns:
            str: Torragon specific attack string
        """
        return f"{self.name} uses Hydro Pump!"
