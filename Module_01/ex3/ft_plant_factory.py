#!/usr/bin/env python3

class Plant:
    """
    Contains the characteristics for the plant
    """
    def __init__(self, name: str, start_height: int, start_age: int):
        self.name = name
        self.start_height = start_height
        self.start_age = start_age

    def print_plant(self) -> None:
        """Prints the plant data in the specified format

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant

        Return:
            None
        """
        print(f"{self.name.capitalize()} ({self.start_height} cm, "
              f"{self.start_age} days old)")


def print_plants_list(plants_list: list[Plant]):
    i: int = 0
    while i < len(plants_list):
        print("Created: ", end="")
        plants_list[i].print_plant()
        i += 1


if __name__ == "__main__":
    rose: Plant = Plant("rose", 25, 30)
    oak: Plant = Plant("oak", 200, 365)
    cactus: Plant = Plant("cactus", 5, 90)
    sunflower: Plant = Plant("sunflower", 80, 45)
    fern: Plant = Plant("fern", 15, 120)
    plants_list: list[Plant] = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    print_plants_list(plants_list)
    print("")
    print(f"Total plants created: {len(plants_list)}")
