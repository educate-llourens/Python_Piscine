#!/usr/bin/env python3

from typing import List


def artifact_sorter(artifacts: List[dict]) -> List[dict]:
    sorted_artifacts: List[dict] = sorted(artifacts,
                                          key=(lambda artifact:
                                               artifact["power"]),
                                          reverse=True)
    return sorted_artifacts


def power_filter(mages: List[dict], min_power) -> List[dict]:
    filtered_mages: List[dict]

    filtered_mages = list(filter(lambda mage: mage['power'] >= min_power, mages))
    return filtered_mages


def spell_transformer(spells: List[str]) -> List[str]:
    transformed_spells: List[str]

    transformed_spells = list(map(lambda spell: "*" + spell + "*", spells))
    return transformed_spells


def mage_stats(mages: List[dict]) -> dict:
    power_info: dict = {}
    powers: List[int] = list(map(lambda mage: mage['power'], mages))

    power_info = {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': sum(powers) / len(mages)
    }
    return power_info


def main() -> None:
    # Variables ***************************************************************
    artifacts: List[dict]
    mages: List[dict]
    sorted_artifacts: List[dict]
    filtered_mages: List[dict]
    transformed_spells: List[str]
    power_stats: dict

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

    # Testing spell transformer ***********************************************
    print("Testing spell transformer...")
    transformed_spells = spell_transformer(["fireball", "heal", "shield"])

    for spell in transformed_spells:
        print(f"{spell} ", end="")
    print("")

    # Testing Power Filter ****************************************************
    mages = [
        {'name': 'Ember', 'power': 59, 'element': 'fire'},
        {'name': 'Storm', 'power': 57, 'element': 'shadow'},
        {'name': 'Phoenix', 'power': 77, 'element': 'earth'}]
    filtered_mages = power_filter(mages, 59)

    print("\nTesting power filter with min power 59. Expect 2 mages...")
    for mage in filtered_mages:
        print(f"{mage['name']} has power {mage['power']}")
    print("")

    # Testing Mage Stats ******************************************************
    mages = [
        {'name': 'Ember', 'power': 59, 'element': 'fire'},
        {'name': 'Storm', 'power': 57, 'element': 'shadow'},
        {'name': 'Phoenix', 'power': 77, 'element': 'earth'}]
    power_stats = mage_stats(mages)

    print("Testing Mage Stats. Expect the following format:")
    print("Max power: 77")
    print("Min power: 57")
    print("Average power: 64.33")
    print("Test:")
    print(f"Max power: {power_stats['max_power']}")
    print(f"Min power: {power_stats['min_power']}")
    print(f"Average power: {power_stats['avg_power']:.2f}")


if __name__ == "__main__":
    main()
