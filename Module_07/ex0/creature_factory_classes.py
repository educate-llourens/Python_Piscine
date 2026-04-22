#!/usr/bin/env python3

from abc import ABC, abstractmethod
from .creature_classes import Flameling, Pyrodon, Aquabub, Torragon, Creature


class CreatureFactory(ABC):
    """Create the base Creature and the evolved Creature for the same family
    """
    @abstractmethod
    def create_base(self) -> Creature:
        """Calls for the first evolution of Flame or Water type

        Returns:
            Creature: Returns the base creature object
        """
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Calls for the evolved version of Flame or Water type

        Returns:
            Creature: Returns the evolved creature object
        """
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
