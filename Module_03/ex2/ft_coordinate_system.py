#!/usr/bin/env python3

import math
import sys


def find_distance(end_position: tuple) -> float:
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

    end_x, end_y, end_z = end_position
    distance = math.sqrt((end_x - 0)**2
                         + (end_y - 0)**2
                         + (end_z - 0)**2)
    return distance


def valid_coordinates(coordinates: tuple) -> None:
    print('Parsing coordinates: "3,4,0"')
    print(f"Parsed position: {coordinates}")


def parse_args() -> tuple:
    coordinates: list = []
    str_list: list[str] = []

    if len(sys.argv) <= 1:
        print("\033[31mError: Not enough arguments. "
              "Please enter a coordinate\033[0m")
        return (10, 20, 5)

    if (len(sys.argv) == 2):
        str_list = sys.argv[1].split(",")
    else:
        for arg in sys.argv[1:]:
            str_list.append(arg)
    for item in str_list:
        try:
            int(item)
            coordinates.append(item)
        except ValueError as msg:
            print(f"\033[31mError parsing coordinates: {msg}")
            print(f"Error details - Type: {type(msg).__name__}, "
                  f'Args: ("{msg}",)\033[0m')
    return tuple(coordinates)


def main() -> None:
    coordinates: tuple = ()
    print("=== Game Coordinate System ===\n")
    coordinates = parse_args()
    print_distance = 3,4,0


if __name__ == "__main__":
    main()
