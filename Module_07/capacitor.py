#!/usr/bin/env python3

from .ex1.capability_factory_classes import (HealingCreatureFactory,
                                             TransformCreatureFactory)


def capacitor() -> None:
    # Variables ***************************************************************
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()
    first_heal_evolution = healing_factory.create_base()
    heal_evolved = healing_factory.create_evolved()
    first_transform_evolution = transform_factory.create_base()
    transform_evolved = transform_factory.create_evolved()

    # Testing base creature with healing ability ******************************
    print("Testing Creature with healing capability")
    print(" base:")
    print(f"{first_heal_evolution.describe()}")
    print(f"{first_heal_evolution.attack()}")
    print(f"{first_heal_evolution.h}")


if __name__ == "__main__":
    capacitor()
