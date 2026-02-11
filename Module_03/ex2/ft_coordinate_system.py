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


def parse_args() -> tuple:
    coordinates: tuple = ()
    str_list: list[str] = []

    if len(sys.argv) <= 1:
        print("\033[31mError: Not enough arguments. "
              "Please enter a coordinate\033[0m")

    if (len(sys.argv) == 2):
        str_list = sys.argv[1].split(",")
    else:
        for arg in sys.argv[1:]:
            str_list.append(arg)
    for item in str_list:
        try:
            int(item)
        except ValueError as msg:
            print(f"Error parsing coordinates: {msg}")
            print(f"Error details - Type: {type(msg).__name__}, "
                f'Args: ("{msg}",)')

    return coordinates


def hard_coded_pos() -> None:
    print("Position created: (10, 20, 5)")
    distance: tuple = (10, 20, 5)
    print(f"Distance between (0, 0, 0) and (10, 20, 5): "
          f"{find_distance(distance):.2f}\n")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    parse_args()
    hard_coded_pos()


if __name__ == "__main__":
    main()
