#!/usr/bin/env python3

def main() -> None:
    """The main function for the program that does the calculations and
    prints the things
    """
    print("=== Achievement Tracker System ===\n")
    alice: set[str] = set(['first_kill', 'level_10', 'treasure_hunter',
                           'speed_demon'])
    bob: set[str] = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie: set[str] = set(['level_10', 'treasure_hunter', 'boss_slayer',
                             'speed_demon', 'perfectionist'])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unique_achievements: set[str] = alice.union(bob, charlie)
    total_unique_achievements: int = len(unique_achievements)
    common_achievements: set[str] = alice.intersection(bob, charlie)
    rare_achievements: set[str] = set()
    rare_achievements = rare_achievements.union(alice.difference(bob, charlie))
    rare_achievements = rare_achievements.union(bob.difference(alice, charlie))
    rare_achievements = rare_achievements.union(charlie.difference(alice, bob))

    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print("")
    print(f"Common to all players: {common_achievements}")
    print(f"Rare achievements (1 player): {rare_achievements}")
    print("")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
