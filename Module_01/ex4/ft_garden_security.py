#!/usr/bin/env python3

class SecurePlant:
    """
    Sets the values for the characteristics of the plants in a safe manner
    """
    def __init__(self, name: str, start_height: int, start_age: int):
        self.name = name
        self.__start_height = start_height
        self.__start_age = start_age

    def set_height(self, new_height: int) -> int:
        """Checks the new height is safe and sets the new height.
            "The General Sherman Tree is the world's largest tree,
             measured by volume. It stands 275 feet (83 m) tall,
             and is over 36 feet (11 m) in diameter."

        Args:
            new_height (int): The new height that is given

        Returns:
            int: Returns -1 if the new height is not a safe value
            or it returns 0 if it successfully set the height
        """
        if new_height < 0:
            return -1
        self.__start_height = new_height
        return 0

    def set_age(self, new_age: int) -> int:
        """Checks the new age is safe and sets the new age

        Args:
            new_age (int): The new age that is given

        Returns:
            int: Returns -1 if the new height is not a safe value
            or it returns 0 if it successfully set the height
        """
        if new_age < 0:
            return -1
        self.__start_age = new_age
        return 0

    def get_height(self) -> int:
        """Retrieves the height

        Returns:
            int: returns the height of the plant
        """
        return self.__start_height

    def get_age(self) -> int:
        """Retrieves the age

        Returns:
            int: Returns the height of the plant
        """
        return self.__start_age

    def get_name(self) -> str:
        return self.name


def print_height_result(plant: SecurePlant, height: int) -> None:
    """Sets the height and prints [OK] if it is a valid change or
       an error message with [REJECTED] if it is an invalid change

    Args:
        plant (SecurePlant): The plant class that the changes wil apply to
        height (int): The height to be changed
    """
    if plant.set_height(height) == 0:
        print(f"Height updated: {height}cm", end=" ")
        print("[OK]")
    elif plant.set_height(height) == -1:
        print("Invalid operation attempted: ", end=" ")
        print(f"height {height}", end=" ")
        print("[REJECTED]")
        print("Security: Negative height rejected")


def print_age_result(plant: SecurePlant, age: int) -> None:
    """Gets the age and prints [OK] if it is a valid change or
       an error message with [REJECTED] if it is an invalid change

    Args:
        plant (SecurePlant): The plant class that the changes wil apply to
        age (int): The age to be changed
    """
    if plant.set_age(age) == 0:
        print(f"Age updated: {age} days", end=" ")
        print("[OK]")
    elif plant.set_age(age) == -1:
        print("Invalid operation attempted: ", end=" ")
        print(f"age {age}", end=" ")
        print("[REJECTED]")
        print("Security: Negative age rejected")


if __name__ == "__main__":
    rose: SecurePlant = SecurePlant("rose", 25, 30)
    current_plant: SecurePlant = rose
    print("=== Garden security System ===")
    print(f"Plant created: {rose.get_name().capitalize()}")
    print_height_result(rose, 25)
    print_age_result(rose, 30)
    print("")
    print_height_result(rose, -5)
    print("")
    print(f"Current plant: {current_plant.name}", end="")
    plant_start_height = current_plant.get_height()
    plant_age = current_plant.get_age()
    print(f"({plant_start_height}cm, {plant_age} "
          f"days)")
