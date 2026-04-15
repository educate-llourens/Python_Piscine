#!/usr/bin/env python3

import alchemy.transmutation


def transmutation_1() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}")


if __name__ == "__main__":
    transmutation_1()
