#!/usr/bin/env python3

import math


class Plant:
    """Class containing the name, height and age of the plant
    """
    def __init__(self, name: str, height: int, age: int):
        """Creates an instance of the Plant class (a plant).

        Args:
            name (str): Name of the plant
            height (int): Height of the plant in cm
            age (int): Age of the plant in days
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """Class that inherits from Plant

    Args:
        Plant (Parent): The parent class
    """
    def __init__(self, name: str, height: int, age: int,
                 colour: str, bloom: bool):
        """Creates an instance from the Flower class (a flower).

        Args:
            name (str): Name of the Flower
            height (int): Height of the Flower in cm
            age (int): Age of the Flower in days
            colour (str): Colour of the Flower when it blooms
            bloom (bool): If it is blooming or not
        """
        super().__init__(name, height, age)
        self.colour: str = colour
        self.bloom: bool = bloom


class Tree(Plant):
    """Class that inherits from plant

    Args:
        Plant (Parent): The parent class
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int, produce_shade: bool):
        """Creates an instance from the Tree class (a tree).

        Args:
            name (str): Name of the Tree
            height (int): Height of the Tree
            age (int): Age of the Tree in cm
            trunk_diameter (int): Diamaeter of the trunk in cm
            produce_shade (bool): Signals if the tree can produce shade or not
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter
        self.produce_shade: bool = produce_shade

    def shade_area(self) -> int:
        """Calculates the area of shade that the tree produces

        Returns:
            int: Returns the area of shade in meters squared
        """
        diameter_m: float = self.trunk_diameter / 100
        crown_radius: float = diameter_m * 10
        area: float = math.pi * crown_radius ** 2
        shade_area: int = math.floor(area)
        return shade_area


class Vegetable(Plant):
    """Class that inherits from Plant

    Args:
        Plant (Parent): The Parent class it inherits from
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        """Creates an instance from the Vegetable class (a vegetable)

        Args:
            name (str): Name of the Vegetable
            height (int): Height of the Vegetable in cm
            age (int): Age of the Vegetable in days
            harvest_season (str): The best season to harvest the Vegetable
            nutritional_value (str): The nutritional information for
            the Vegetable
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


def print_plant(plant: Plant) -> None:
    """Prints the basic information for the Plant like name, height and age

    Args:
        plant (Plant): The plant we need to print the information for
    """
    print(f"\n{plant.name.capitalize()} ({plant.__class__.__name__}): "
          f"{plant.height}cm, "
          f"{plant.age} days", end=", ")


def print_flower(flower: Flower) -> None:
    """Prints information for the flower

    Args:
        flower (Flower): The flower that we need to print the information for
    """
    print_plant(flower)
    print(f"{flower.colour} colour")
    if flower.bloom:
        print(f"{flower.name.capitalize()} is blooming beautifully!")


def print_tree(tree: Tree) -> None:
    """Prints information for the tree

    Args:
        tree (Tree): The tree that we need to print the information for
    """
    print_plant(tree)
    print(f"{tree.trunk_diameter}cm diameter")
    if tree.produce_shade:
        print(f"{tree.name.capitalize()} provides {tree.shade_area()} "
              f"square meters of shade")


def print_vegetable(veg: Vegetable):
    """Prints information for the vegetable

    Args:
        veg (Vegetable): The vegetable that we need to print the
        information for
    """
    print_plant(veg)
    print(f"{veg.harvest_season} harvest")
    print(f"{veg.name.capitalize()} is {veg.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    # Flowers
    rose = Flower("rose", 25, 30, "red", True)
    bluebell = Flower("bluebell", 15, 20, "blue", False)

    # Trees
    oak = Tree("oak", 500, 1825, 50, True)
    ash = Tree("ash", 350, 2000, 30, False)

    # Vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    carrot = Vegetable("Carrot", 12, 15, "autumn", "rich in Vitamin A")

    print_flower(rose)
    print_flower(bluebell)
    print_tree(oak)
    print_tree(ash)
    print_vegetable(tomato)
    print_vegetable(carrot)
