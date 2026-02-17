#!/usr/bin/env python3

import math
import sys


def len_str(list: list[str]) -> int:
    length: int = 0

    for item in list:
        length += 1
    return length


def len_nbrs(list: list[int]) -> int:
    length: int = 0

    for item in list:
        length += 1
    return length


def append_int(nbr_list: list[int], nbr: int) -> list[int]:
    new_list: list[int] = []

    if not nbr_list:
        new_list += [nbr]
        return new_list

    for item in nbr_list:
        new_list += [item]
    new_list += [nbr]
    return new_list


def append_str(str_list: list[str], string: str) -> list[str]:
    new_list: list[str] = []

    if not str_list:
        new_list += [string]
        return new_list

    for item in str_list:
        new_list += [item]
    new_list += [string]
    return new_list


def find_distance(end_position: tuple[int, ...]) -> float:
    """Finds the distance between the start position and the end position.
    Uses unpacking here instead of in the "demonstration".

    Args:
        end_position (tuple): The x, y and z coordinates away from
        start position

    Returns:
        float: The distance up to 2 decimals
    """
    end_x: int
    end_y: int
    end_z: int

    try:
        end_x, end_y, end_z = end_position
        distance = math.sqrt((end_x - 0)**2 + (end_y - 0)**2 + (end_z - 0)**2)
    except ValueError as msg:
        print(f"\033[31mError: {msg}\033[0m\n")
        distance = 0
    return distance


def valid_coordinates() -> None:
    print('Parsing coordinates: "3,4,0"')
    print('Parsed position: "3,4,0"')


def parse_args(args: list[str]) -> tuple[int, ...]:
    """Parses the command line arguments and either throws an error
    or places the coordinate into a tuple of type int

    Args:
        args (list[str]): The coordinate as a list of strings

    Returns:
        tuple[int, int, int]: Returns a tuple with the int
        coordinate
    """
    coordinates: list[int] = []

    for item in args:
        try:
            int(item)
            coordinates = append_int(coordinates, int(item))
        except ValueError as msg:
            print(f"\033[31mError parsing coordinates: {msg}")
            print(f"Error details - Type: {type(msg).__name__}, "
                  f'Args: ("{msg}",)\033[0m')
            return (10, 20, 5)
    return tuple(coordinates)


def print_len_error() -> None:
    print("\033[31mError: Not enough arguments. "
          'Please enter a coordinate. Usage: 3 2 1 or "3,2,1"')
    print('Template coordinate: "10,20,5"\033[0m\n')


def main() -> None:
    arg_len: int = len_str(sys.argv[1:])
    parse_list: list[str] = []
    if arg_len <= 0:
        print_len_error()
        parse_list = ["10", "20", "5"]
    elif arg_len == 1:
        parse_list = sys.argv[1].split(",")
    elif arg_len == 3:
        parse_list: list[str] = sys.argv[1:]
    else:
        print('Too many arguments. Usage: 3 2 1 or "3,2,1')
    coordinates: tuple[int, ...] = parse_args(parse_list)

    print("=== Game Coordinate System ===\n")
    print(f"Position created {coordinates}")
    print(f"Distance between (0, 0, 0) and {coordinates}: "
          f"{find_distance(coordinates):.2f}")
    print("")

    print('Parsing coordinates: "3,4,0"')
    parse_valid_args: list[str] = ["3", "4", "0"]

    coordinates = parse_args(parse_valid_args)
    print(f"Parsed position: {coordinates}")
    print(f"Distance between (0, 0, 0) and (3, 4, 0): "
          f"{find_distance(coordinates):.2f}")
    print("")

    print('Parsing invalid coordinates: "abc,def,ghi"')
    parse_invalid_args: list[str] = ["abc", "def", "ghi"]

    parse_args(parse_invalid_args)
    print("")

    print("Unpacking demonstration:")
    print("Player at x=3, y=4, z=0")
    unpacked_coordinates: tuple[int, ...] = (3, 4, 0)
    end_x: int
    end_y: int
    end_z: int

    end_x = unpacked_coordinates[0]
    end_y = unpacked_coordinates[1]
    end_z = unpacked_coordinates[2]

    print(f"Coordinates: X={end_x}, Y={end_y}, Z={end_z}")


if __name__ == "__main__":
    main()
