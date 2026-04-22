#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import cast
from ex0.creature_classes import Creature
from ex1.capability_classes import HealCapability, TransformCapability


class BattleStrategy(ABC):
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
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            transform_creature = cast(TransformCapability, creature)
            return (f"{transform_creature.transform()}\n"
                    f"{creature.attack()}\n"
                    f"{transform_creature.revert()}")
        raise ValueError("Battle error, aborting tournament: "
                         f"Invalid Creature '{creature.name}' for this "
                         "agrssive strategy")
        return ""


class DefensiveStrategy(BattleStrategy):
    """Suitable for Creature with healing capabilities, that
will attack and then heal during the tournament.
    """
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            healing_creature: HealCapability = cast(HealCapability, creature)
            return (f"{creature.attack()}\n"
                    f"{healing_creature.heal()}")
        raise ValueError("Battle error, aborting tournament: "
                         f"Invalid Creature '{creature.name}' for this "
                         "defensive strategy")
        return ""
