#!/usr/bin/env python3

from typing import List, Tuple
from ex0.creature_classes import Creature
from ex0.creature_factory_classes import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import battle_strategy_classes
from ex2.battle_strategy_classes import BattleStrategy


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    opp_1: int

    for opp_1 in range(len(opponents)):
        for opp_2 in range(opp_1 + 1, len(opponents)):
            factory_1, strategy_1 = opponents[opp_1]
            factory_2, strategy_2 = opponents[opp_2]
            opponent_1: Creature = factory_1.create_base()
            opponent_2: Creature = factory_2.create_base()
            print("* Battle *")
            print(f"{opponent_1.describe()}")
            print(" vs.")
            print(f"{opponent_2.describe()}")
            print(" now fight!")
            try:
                print(f"{strategy_1.act(opponent_1)}")
                print(f"{strategy_2.act(opponent_2)}\n")
            except ValueError as msg:
                raise ValueError(msg)


def tournament() -> None:
    # Variables ***************************************************************
    opponents: List[Tuple[CreatureFactory, BattleStrategy]] = []

    # Tournament 0 -> Basic tournament ****************************************

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament **")
    opponents = [(FlameFactory(), battle_strategy_classes.NormalStrategy()),
                 (HealingCreatureFactory(),
                  battle_strategy_classes.DefensiveStrategy())]
    print(f"{len(opponents)} opponents involved\n")
    try:
        battle(opponents)
    except ValueError as msg:
        print(f"{msg}\n")

    # Tournament 1 -> Error test **********************************************
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    opponents = [(FlameFactory(),
                  battle_strategy_classes.AggressiveStrategy()),
                 (HealingCreatureFactory(),
                  battle_strategy_classes.DefensiveStrategy())]
    print(f"{len(opponents)} opponents involved\n")
    try:
        battle(opponents)
    except ValueError as msg:
        print(f"{msg}\n")

    # Tournament 2 -> multiple opponents **************************************
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    opponents = [(AquaFactory(), battle_strategy_classes.NormalStrategy()),
                 (HealingCreatureFactory(),
                  battle_strategy_classes.DefensiveStrategy()),
                 (TransformCreatureFactory(),
                  battle_strategy_classes.AggressiveStrategy())]
    print(f"{len(opponents)} opponents involved\n")
    try:
        battle(opponents)
    except ValueError as msg:
        print(f"{msg}\n")


if __name__ == "__main__":
    tournament()
