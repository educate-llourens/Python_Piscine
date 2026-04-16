#!/usr/bin/env python3

from ex0.creature_classes import Creature
from ex0.creature_factory_classes import CreatureFactory
from ex1.creature_and_capability_classes import (Sproutling, Bloomelle,
                                                 Shiftling, Morphagon,
                                                 HealCapability,
                                                 TransformCapability)


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
