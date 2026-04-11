#!/usr/bin/env python3

import alchemy


def alambic_4() -> None:
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.elements.create_air()}")


if __name__ == "__main__":
    alambic_4()