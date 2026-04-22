#!/usr/bin/env python3

from ex0.creature_factory_classes import FlameFactory, AquaFactory
from ex0.creature_classes import (Creature)


def battle() -> None:
    # Variables ***************************************************************
    flame_creature_factory: FlameFactory = FlameFactory()
    aqua_creature_factory: AquaFactory = AquaFactory()
    flame_first_evolution: Creature = flame_creature_factory.create_base()
    flame_evolved: Creature = flame_creature_factory.create_evolved()
    aqua_first_evolution: Creature = aqua_creature_factory.create_base()
    aqua_evolved: Creature = aqua_creature_factory.create_evolved()

    # Testing FlameFactory ****************************************************
    print("Testing factory")
    print(f"{flame_first_evolution.describe()}")
    print(f"{flame_first_evolution.attack()}")
    print(f"{flame_evolved.describe()}")
    print(f"{flame_evolved.attack()}\n")

    # Testing AquaFactory *****************************************************
    print("Testing factory")
    print(f"{aqua_first_evolution.describe()}")
    print(f"{aqua_first_evolution.attack()}")
    print(f"{aqua_evolved.describe()}")
    print(f"{aqua_evolved.attack()}\n")

    # Testing battle
    print("Testing battle")
    print(f"{flame_first_evolution.describe()}")
    print(" vs.")
    print(f"{aqua_first_evolution.describe()}")
    print(" fight!")
    print(f"{flame_first_evolution.attack()}")
    print(f"{aqua_first_evolution.attack()}")


if __name__ == "__main__":
    battle()
