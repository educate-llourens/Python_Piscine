#!/usr/bin/env python3

def water_plants(plant_list: list[str]) -> None:
    """
    Checks the plants list for errors. It waters the plants if
    there is no error and it "cleans up resources" regardless
    of if there is a failure

    Args:
        plant_list (list[str]): List of plant names
    """
    print("Opening water system")
    i: int = 0
    try:
        for i in range(0, len(plant_list)):
            plant_list[i].isalpha()
            print(f"Watering {plant_list[i]}")
    except (AttributeError, ValueError):
        print(f"Error: Cannot water {plant_list[i]} - invalid plant!")
    finally:
        print("Closing water system (cleanup)")
    if i == len(plant_list) - 1:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Tests the water_plants function with normal and error values.

    """
    print(" === Garden Watering System ===")
    print("\nTesting normal watering...")
    plants_list: list[str] = ["tomato", "lettuce", "carrots"]
    water_plants(plants_list)
    plants_list = ["tomato", None, "carrots"]
    print("\nTesting with error...")
    water_plants(plants_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
