#!/usr/bin/env python3

class Plant:
    """
    Contains the characteristics for the plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Contins the data and behaviour of a plant

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant
        """
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self) -> None:
        """Prints the plant data in the specified format

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant
        """
        print(f"{self.name.capitalize()}: {self.height} cm, "
              f"{self.age} days old")


if __name__ == "__main__":
    rose: Plant = Plant("rose", 25, 30)
    sunflower: Plant = Plant("sunflower", 80, 45)
    cactus: Plant = Plant("cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.print_plant()
    sunflower.print_plant()
    cactus.print_plant()
