#!/usr/bin/env python3

from typing import List
from ex0 import creature_classes
from ex0.creature_classes import Creature
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import battle_strategy_classes
from ex2.battle_strategy_classes import BattleStrategy


def tournament() -> None:
    # Variables ***************************************************************
    opponents: List[creature_classes.Creature] = []
    flame_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()
    opponent_flameling: Creature = flame_factory.create_base()
    opponent_aquabub: Creature = aqua_factory.create_base()
    opponent_sproutling: Creature = healing_factory.create_base()
    opponent_shiftling: Creature = transform_factory.create_base()
    flameling_strategy: BattleStrategy = (
        battle_strategy_classes.NormalStrategy())
    sproutling_strategy: BattleStrategy = (
        battle_strategy_classes.DefensiveStrategy())
    aquabub_strategy: BattleStrategy = battle_strategy_classes.NormalStrategy()
    shiftling_strategy: BattleStrategy = (
        battle_strategy_classes.AggressiveStrategy())

    # Tournament 0 -> Basic tournament ****************************************

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament **")
    opponents = [opponent_flameling, opponent_sproutling]
    print(f"{len(opponents)} opponents involved\n")

    print("* Battle *")
    print(f"{opponent_flameling.describe()}")
    print(" vs.")
    print(f"{opponent_sproutling.describe()}")
    print(" now fight!")
    print(f"{flameling_strategy.act(opponent_flameling)}")
    print(f"{sproutling_strategy.act(opponent_sproutling)}\n")

    # Tournament 1 -> Error test **********************************************
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    flameling_strategy = battle_strategy_classes.AggressiveStrategy()
    print(f"{len(opponents)} opponents involved\n")

    print("* Battle *")
    print(f"{opponent_flameling.describe()}")
    print(" vs.")
    print(f"{opponent_sproutling.describe()}")
    print(" now fight!")
    try:
        print(f"{flameling_strategy.act(opponent_flameling)}")
        print(f"{sproutling_strategy.act(opponent_sproutling)}\n")
    except ValueError as msg:
        print(f"{msg}\n")

    # Tournament 2 -> multiple opponents **************************************
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    opponents = [opponent_aquabub, opponent_sproutling, opponent_shiftling]
    print(f"{len(opponents)} opponents involved\n")

    print("* Battle *")
    print(f"{opponent_aquabub.describe()}")
    print(" vs.")
    print(f"{opponent_sproutling.describe()}")
    print(" now fight!")
    try:
        print(f"{aquabub_strategy.act(opponent_aquabub)}")
        print(f"{sproutling_strategy.act(opponent_sproutling)}\n")
    except ValueError as msg:
        print(f"{msg}\n")

    print("* Battle *")
    print(f"{opponent_aquabub.describe()}")
    print(" vs.")
    print(f"{opponent_shiftling.describe()}")
    print(" now fight!")
    try:
        print(f"{aquabub_strategy.act(opponent_aquabub)}")
        print(f"{shiftling_strategy.act(opponent_shiftling)}\n")
    except ValueError as msg:
        print(f"{msg}\n")

    print("* Battle *")
    print(f"{opponent_sproutling.describe()}")
    print(" vs.")
    print(f"{opponent_shiftling.describe()}")
    print(" now fight!")
    try:
        print(f"{sproutling_strategy.act(opponent_sproutling)}")
        print(f"{shiftling_strategy.act(opponent_shiftling)}")
    except ValueError as msg:
        print(f"{msg}\n")


if __name__ == "__main__":
    tournament()
