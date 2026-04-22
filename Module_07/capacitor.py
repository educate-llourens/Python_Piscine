#!/usr/bin/env python3

from typing import Any
from ex1.capability_factory_classes import (HealingCreatureFactory,
                                            TransformCreatureFactory)


def capacitor() -> None:
    # Variables ***************************************************************
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()
    first_heal_evolution: Any = healing_factory.create_base()
    heal_evolved: Any = healing_factory.create_evolved()
    first_transform_evolution: Any = (
        transform_factory.create_base())
    transform_evolved: Any = transform_factory.create_evolved()

    # Testing creature with healing ability ***********************************
    print("Testing Creature with healing capability")
    print(" base:")
    print(f"{first_heal_evolution.describe()}")
    print(f"{first_heal_evolution.attack()}")
    print(f"{first_heal_evolution.heal()}")
    print(" evolved:")
    print(f"{heal_evolved.describe()}")
    print(f"{heal_evolved.attack()}")
    print(f"{heal_evolved.heal()}\n")

    # Testing creature with transform ability *********************************
    print("Testing Creature with transform capability")
    print(" base:")
    print(f"{first_transform_evolution.describe()}")
    print(f"{first_transform_evolution.attack()}")
    print(f"{first_transform_evolution.transform()}")
    print(f"{first_transform_evolution.attack()}")
    print(f"{first_transform_evolution.revert()}")
    print(" evolved:")
    print(f"{transform_evolved.describe()}")
    print(f"{transform_evolved.attack()}")
    print(f"{transform_evolved.transform()}")
    print(f"{transform_evolved.attack()}")
    print(f"{transform_evolved.revert()}")


if __name__ == "__main__":
    capacitor()
