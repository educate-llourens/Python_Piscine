#!/usr/bin/env python3
GROWTH_RATE = 1


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

        Return:
            None
        """
        print(f"{self.name.capitalize()}: {self.height} cm, "
              f"{self.age} days old")

    def grow(self, nbr_days: int) -> int:
        """Calculates the growth of the plant based on the number of days.
           It is calculated at 1cm per day of growth.

        Args:
            nbr_days (int): the number of days given to grow

        Returns:
            int: The new height of the plant
        """
        self.height += nbr_days * GROWTH_RATE
        return self.height

    def aging(self, nbr_days: int) -> int:
        """Calculates the age of the plant based on the current age of
           the plant and the number of days given to grow.

        Args:
            nbr_days (int): The number of days given to grow.

        Returns:
            int: The new age of the plant
        """
        self.age += nbr_days
        return self.age


def get_info(plant_name: Plant, nbr_days: int) -> Plant:
    """Retrieves and returns the new information for the plant based on
       the number of days to grow.

    Args:
        plant_name (Plant): The plant needing the calulations
        nbr_days (int): The number of days given to grow

    Returns:
        Plant: Returns the plant object with the updated information
    """
    plant_name.height = plant_name.grow(nbr_days)
    plant_name.age = plant_name.aging(nbr_days)
    return plant_name


if __name__ == "__main__":
    start_day: int = 1
    growth_days: int = 6
    rose: Plant = Plant("rose", 25, 30)
    print(f"=== Day {start_day} ===")
    rose.print_plant()
    print(f"=== Day {start_day + growth_days} ===")
    updated_rose: Plant = get_info(rose, growth_days)
    updated_rose.print_plant()
    print(f"Growth this week: +{growth_days * GROWTH_RATE} cm")
