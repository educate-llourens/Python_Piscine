#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature_classes import Creature
from ex1.capability_factory_classes import (HealingCreatureFactory,
                                            TransformCreatureFactory)
from ex1.creature_classes import (Sproutling, Bloomelle, Shiftling, Morphagon)


class BattleStrategy:
    @abstractmethod
    def act(self, creature: Creature) -> str:
        """Will be called by the tournament script

        Returns:
            str: An attack string probably
        """
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """
        Returns:
            bool: True if creature is suitable for the strategy
        """
        pass


class NormalStrategy(BattleStrategy):
    """Suitable for any creature and uses attack method during the tournament
    """
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    """Suitable for transform capability creatures. It will transform, attack
    and revert

    Args:
        BattleStrategy (_type_): _description_
    """
    def is_valid(self, creature: Creature) -> bool:
        if type(creature) is Shiftling or type(creature) is Morphagon:
            return True
        return False

    def act(self, creature: Creature) -> str:
        c


class DefensiveStrategy(BattleStrategy):
    """Suitable for Creature with healing capabilities, that
will attack and then heal during the tournament.
    """
    pass
