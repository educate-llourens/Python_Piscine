#!/usr/bin/env python3

def test_temperature_input() -> None:
    """
    Test function for the check_temperature function
    """
    print("=== Garden Temperature Checker ===\n")

    test_temp: str = "25"
    print(f"Testing temperature: {test_temp}")
    check_temperature(test_temp)

    test_temp: str = "abc"
    print(f"Testing temperature: {test_temp}")
    check_temperature(test_temp)

    test_temp: str = "100"
    print(f"Testing temperature: {test_temp}")
    check_temperature(test_temp)

    test_temp: str = "-50"
    print(f"Testing temperature: {test_temp}")
    check_temperature(test_temp)


def check_temperature(temp_str: str) -> int:
    """
    Check's the paraemeter string to see if it is a valid number
    and within the parameters for a healthy plant.

    Args:
        temp_str (str): The temperature in string form

    Returns:
        int: The valid temperature or None
    """
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None
    if (temp < 0) or (temp > 40):
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
            return None
        else:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
            return None
    print(f"Temperature {temp}°C is perfect for plants!\n")
    return temp


if __name__ == "__main__":
    test_temperature_input()
    print("All tests completed - program didn't crash!")
