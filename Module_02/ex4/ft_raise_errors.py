#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    Checks if the plant name is valid, it has enough water and
    sunlight.

    Args:
        plant_name (str): Name of te plant
        water_level (int): Water level of the plant
        sunlight_hours (int): Number of hours of sunlight it gets

    Raises:
        ValueError(plant name): Name of the plant is None
        ValueError(water level min): Water level is below 1
        ValueError(water level max): Water level is above 10
        ValueError(sunlight hours min): Sunlight hours are less than 2
        ValueError(sunlight hours max): Sunlight hours are more than 12
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        if water_level < 1:
            raise ValueError(f"Error: Water level {water_level} is too low "
                             "(min 1)")
        else:
            raise ValueError(f"Error: Water level {water_level} is too high "
                             "(max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is "
                             "too low (min 2)")
        else:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is "
                             "too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Creates test cases for check_plant_health function
    """
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    check_plant_health("tomato", 3, 4)

    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 3, 4)
    except ValueError as error_msg:
        print(error_msg)

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 4)
    except ValueError as error_msg:
        print(error_msg)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 3, 0)
    except ValueError as error_msg:
        print(error_msg)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
