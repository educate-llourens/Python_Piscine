#!/usr/bin/env python3

def garden_operations(operation_type: str) -> Exception:
    """
    Summary:
        Creates the different types of exceptions that can occur
    Args:
        operation_type (str): The type of exception to test
    Returns:
        Exception: Returns the exception that gets raised
    """
    if operation_type == "Value_Error":
        int('abc')
    elif operation_type == "Zero_Division_Error":
        7 / 0
    elif operation_type == "File_Not_Found_Error":
        open("missing.txt", "r")
    elif operation_type == "Key_Error":
        plants: dict = {"tomato": 32}
        plants["missing_plant"]
    else:
        int('abc')
        7 / 0
        open("missing.txt", "r")
        plants: dict = {"tomato": 32}
        plants["mising_plant"]


def test_error_types() -> None:
    """
    Summary:
        Calls graden_operations and shows how the different
        exceptions get handled.
    """
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("Value_Error")
    except ValueError as error_msg:
        msg: str = str(error_msg)
        precise_msg: str = msg.split("with")[0]
        print("Caught ValueError: ", precise_msg)

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("Zero_Division_Error")
    except ZeroDivisionError as error_msg:
        print("Caught ZeroDivisionError: ", error_msg)

    print("\nTesting FileNotFoundError..")
    try:
        garden_operations("File_Not_Found_Error")
    except FileNotFoundError as error_mesage:
        msg = str(error_mesage)
        precise_msg_1 = msg.split("[Errno 2] ")[1]
        precise_msg_2 = precise_msg_1.split(" or directory: ")[0]
        precise_msg_3 = precise_msg_1.split(" or directory: ")[1]
        print("Caught FileNotFoundError: ", precise_msg_2, precise_msg_3)

    print("\nTesting KeyError..")
    try:
        garden_operations("Key_Error")
    except KeyError as error_msg:
        print("Caught KeyError: ", error_msg)

    print("\nTesting mutiple errors together...")
    try:
        garden_operations("")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    test_error_types()
    print("\nAll error types tested successfully!")
