#!/usr/bin/env python3

def garden_intro(name: str, height: int, age: int) -> None:
    """
    Docstring for garden_intro
    :description: Prints plant information

    :param name: Plant name
    :type name: str
    :param height: Plant height
    :type height: int
    :param age: Plant age
    :type age: int

    :return: None
    """
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height} cm")
    print(f"Age: {age} days")
    print("")
    print("=== End of Program ===")


if __name__ == "__main__":
    garden_intro("Rose", 25, 30)
