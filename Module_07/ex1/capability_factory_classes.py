#!/usr/bin/env python3

from ex0.creature_factory_classes import CreatureFactory
from .creature_classes import (Sproutling, Bloomelle, Shiftling, Morphagon)


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
