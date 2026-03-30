#!/usr/bin/env python3

import alchemy


def main() -> None:
    # Variables ***************************************************************
    pkg_create_fire: str = ""
    pkg_create_water: str = ""
    pkg_create_earth: str = ""
    pkg_create_air: str = ""

    # Direct access ***********************************************************
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}\n")

    # Package level access ****************************************************
    print("Testing package-level access (controlled by __init__.py):")

    # create_fire ---------------------------------------------------
    print("alchemy.create_fire():", end=" ")
    try:
        pkg_create_fire = alchemy.create_fire()
        print(pkg_create_fire)
    except AttributeError:
        print("AttributeError - not exposed")

    # create_water --------------------------------------------------
    print("alchemy.create_water:", end=" ")
    try:
        pkg_create_water = alchemy.create_water()
        print(pkg_create_water)
    except AttributeError:
        print("AttributeError - not exposed")

    # create_earth --------------------------------------------------
    print("alchemy.create_earth:", end=" ")
    try:
        pkg_create_earth = alchemy.create_earth()
        print(pkg_create_earth)
    except AttributeError:
        print("AttributeError - not exposed")

    # create_air ----------------------------------------------------
    print("alchemy.create_air:", end=" ")
    try:
        pkg_create_air = alchemy.create_air()
        print(pkg_create_air)
    except AttributeError:
        print("AttributeError - not exposed\n")

    # Package metadata ********************************************************
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
