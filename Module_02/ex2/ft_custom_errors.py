#!/usr/bin/env python3

class GardenError(Exception):
    """Summary:
        A custom error for garden problems
    """
    pass


class PlantError(GardenError):
    """
    Summary:
        For problems with plants
    Args:
        GardenError (Exception): inherits from GardenError
    """
    def __init__(self, plant_name: str) -> None:
        """Summary:
            Initiates the PlantError instance

        Args:
            plant_name (str): The name of the plant to create an error message
        """
        self.plant_name: str = plant_name
        msg: str = f"The {self.plant_name} is wilting!"
        super().__init__(msg)


class WaterError(GardenError):
    """Summary:
        For problems with water
    Args:
        GardenError (Exception): inherits from GardenError
    """
    def __init__(self) -> None:
        """
        Summary:
            Initiates the WaterError instance

        Args:
            plant_name (str): The name of the plant to create an error message
        """
        msg: str = "Not enough water in the tank!"
        super().__init__(msg)


def garden_operations(error_check: str) -> None:
    """Raises the different custom errors

    Args:
        error_check (str): Takes in the type of error to raise

    Raises:
        PlantError: Prints a description of the PlantError
        WaterError: Prints a description of the WaterError
    """
    if error_check == "Plant_Error":
        raise PlantError("tomato")
    elif error_check == "Water_Error":
        raise WaterError()


def test_error_types() -> None:
    """Creates tests for the different custom errors
    """
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        garden_operations("Plant_Error")
    except PlantError as error_msg:
        print("Caught PlantError:", error_msg)

    print("\nTesting WaterError...")
    try:
        garden_operations("Water_Error")
    except WaterError as error_msg:
        print("Caught WaterError:", error_msg)

    print("\nTesting catching all garden errors...")
    try:
        garden_operations("Plant_Error")
    except GardenError as error_msg:
        print("Caught a garden error:", error_msg)
    try:
        garden_operations("Water_Error")
    except GardenError as error_msg:
        print("Caught a garden error:", error_msg)


if __name__ == "__main__":
    test_error_types()
    print("\nAll custom error types work correctly!")
