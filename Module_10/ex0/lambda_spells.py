#!/usr/bin/env python3

from typing import List


def artifact_sorter(artifacts: List[dict]) -> List[dict]:
    sorted_artifacts: List[dict] = sorted(artifacts,
                                          key=(lambda artifact:
                                               artifact["power"]),
                                          reverse=True)
    return sorted_artifacts


# def power_filter(mages: List[dict], min_power) -> List[dict]:
#     sorted_mages: List[dict] = []
#     return sorted_mages


def spell_transformer(spells: List[str]) -> List[str]:
    transformed_spells: List[str]

    transformed_spells = list(map(lambda spell: "*" + spell + "*", spells))
    return transformed_spells


# def mage_stats(mages) -> dict:
#     power_info: dict = {}
#     return power_info


def main() -> None:
    # Variables ***************************************************************
    artifacts: List[dict]
    sorted_artifacts: List[dict]
    transformed_spells: List[str]

    # Testing artifact sorter *************************************************
    artifacts = [{'name': 'Shadow Blade', 'power': 119, 'type': 'focus'},
                 {'name': 'Shadow Blade', 'power': 78, 'type': 'armor'},
                 {'name': 'Fire Staff', 'power': 90, 'type': 'accessory'}
                 ]
    sorted_artifacts = artifact_sorter(artifacts)
    print("\nTesting artifact sorter...")
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} "
          f"power) comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']})\n")

    print("Testing spell transformer...")
    transformed_spells = spell_transformer(["fireball", "heal", "shield"])
    for spell in transformed_spells:
        print(f"{spell} ", end="")
    print("")


if __name__ == "__main__":
    main()
