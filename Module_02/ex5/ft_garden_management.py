#!/usr/bin/env python3

class GardenError(Exception):
    """Initiates the Garden Exception class

    Args:
        Exception (_type_): GardenError is an Exception
    """
    pass


class WaterError(GardenError):
    """Prints an error message depending on the type of
    water error

    Args:
        GardenError (_type_): Inherits from GardenError
    """
    def __init__(self, water_level: int | None = None):
        """Initiates the water error class with the water level or None

        Args:
            water_level (int | None, optional): The water level of the plant.
            Defaults to None if an int is not given
        """
        self.water_level = water_level
        if self.water_level is None:
            msg = "Not enough water in tank"
        elif self.water_level < 1:
            msg: str = (f"Water level {water_level} is too "
                        + "low (min 1)")
        elif self.water_level > 10:
            msg = (f"Water level {water_level} is too "
                   + "high (max 10)")
        super().__init__(msg)


class SunError(GardenError):
    """Prints an error message depending on the type of
    sun error

    Args:
        GardenError (_type_): Inherits from GardenError
    """
    def __init__(self, sun_hours: int):
        """Initiates the SunError class with the number of
        hours the plant gets sun

        Args:
            sun_hours (int): The number of hours of sun the plant gets
        """
        self.sun_hours = sun_hours
        if sun_hours < 2:
            msg: str = f"Sunlight hours {sun_hours} is too "
            + "low (min 2)"
        else:
            msg = f"Sunlight hours {sun_hours} is too "
            + "high (max 12)"
        super().__init__(msg)


class Plant:
    """Contains information on the plant like the name, water level and number
    of hours it gets sun
    """
    def __init__(self, plant_name: str, water_level: int, sun_hours: int):
        """Creates a plant object

        Args:
            plant_name (str): Name of the plant
            water_level (int): Water level of the plant
            sun_hours (int): Number of hours of sun the plant gets
        """
        self.plant_name = plant_name
        self.water_level = water_level
        self.sun_hours = sun_hours


class GardenManager:
    """Allows the manager to add plants, water the garden and check on
    the health of each plant in the garden
    """
    def __init__(self):
        """Creates a garden manager that can control a garden
        """
        self.plants_list: list[Plant] = []
        self.plant_list_len = len(self.plants_list)
        self.water_in_tank: bool = True

    def add_plants(self, plant: Plant) -> None:
        """Allows the manager to add a plant to the garden

        Args:
            plant (Plant): The plant object that needs to be added to
            the garden

        Raises:
            ValueError: If the name does not exist it creates a ValueError
            telling the user that a plant name is compulsory
        """
        if not plant or not plant.plant_name:
            raise ValueError("Plant name cannot be empty!")
        self.plants_list.append(plant)
        self.plant_list_len += 1
        print(f"Added {plant.plant_name} successfully")

    def water_plants(self) -> None:
        """Allows the manager to water the plants in the garden

        Raises:
            WaterError: If there in not enough water in the tank it raises
            a WaterError
        """
        if self.water_in_tank is False:
            raise WaterError()
        print("Opening watering system")
        i: int = 0
        for i in range(0, self.plant_list_len):
            print(f"Watering {self.plants_list[i].plant_name} - success")

    def checking_plant_health(self, plant: Plant) -> None:
        """Allows the manager to check on the health of the plant

        Args:
            plant (Plant): The plant that the manager is checking

        Raises:
            WaterError: If the plant water level is too high or too low
            SunError: If the number of hours of sun it receives is too
            much or too little
        """
        if plant.water_level < 1 or plant.water_level > 10:
            raise WaterError(plant.water_level)
        sun_level = plant.sun_hours
        if plant.sun_hours < 2 or plant.sun_hours > 12:
            raise SunError(sun_level)
        print(f"{plant.plant_name}: healthy (water: {plant.water_level}, "
              f"sun: {plant.sun_hours})")


def garden_tester() -> None:
    """Creates the tests for my Garden Management System
    """
    alice = GardenManager()
    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    try:
        alice.add_plants(Plant("tomato", 5, 8))
    except ValueError as msg:
        print("Error adding plant:", msg)
    try:
        alice.add_plants(Plant("lettuce", 15, 8))
    except ValueError as msg:
        print("Error adding plant:", msg)
    try:
        alice.add_plants(None)
    except ValueError as msg:
        print("Error adding plant:", msg)

    print("\nWatering plants...")
    try:
        alice.water_plants()
    except WaterError as error_msg:
        print("Error:", error_msg)
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    i: int = 0
    for i in range(0, alice.plant_list_len):
        try:
            alice.checking_plant_health(alice.plants_list[i])
        except (WaterError, SunError) as error_msg:
            print(f"Error checking {alice.plants_list[i].plant_name}:",
                  error_msg)

    print("\nTesting error recovery...")
    alice.water_in_tank = False
    try:
        alice.water_plants()
    except GardenError as error_msg:
        print("Caught GardenError:", error_msg)
    print("System recovered and still continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    garden_tester()
