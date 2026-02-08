#!/usr/bin/env python3


class Plant:
    """Class containing the name, height and age of the plant
    """
    def __init__(self, name: str, height: int):
        """Creates an instance of the Plant class (a plant).

        Args:
            name (str): Name of the plant
            height (int): Height of the plant in cm
            age (int): Age of the plant in days
        """
        self.name: str = name
        self.height: int = height


class Flower(Plant):
    """Class that inherits from Plant

    Args:
        Plant (Parent): The parent class
    """
    def __init__(self, name: str, height: int,
                 colour: str, bloom: bool):
        """Creates an instance from the Flower class (a flower).

        Args:
            name (str): Name of the Flower
            height (int): Height of the Flower in cm
            age (int): Age of the Flower in days
            colour (str): Colour of the Flower when it blooms
            bloom (bool): If it is blooming or not
        """
        super().__init__(name, height)
        self.colour: str = colour
        self.bloom: bool = bloom


class PrizeFlower(Flower):
    """Class that inherits from Flower

    Args:
        Flower (Plant): The parent class
    """
    def __init__(self, name: str, height: int,
                 colour: str, bloom: bool, points: int):
        """Creates an instance of PrizeFlower (a prized flower)

        Args:
            name (str): Name of the prized flower
            height (int): Height of the prized flower
            colour (str): Colour of the prized flower when it blooms
            bloom (bool): If it is blooming or not
            points (int): The number of points awarded to the flower
        """
        super().__init__(name, height, colour, bloom)
        self.points: int = points


class GardenManager:
    """A class for the manager that manages all the gardens within it
    """
    def __init__(self, name: str):
        """Creates an instance of the GardenManager (a manager)

        Args:
            name (str): Name of the manager
        """
        self.name: str = name
        self.gardens: list[GardenManager.Garden] = []
        self.manager_stats: GardenManager.GardenStats = self.GardenStats(self)

    class Garden:
        """A class for managing a garden
        """
        def __init__(self, garden_name: str, manager: 'GardenManager'):
            """Creates an instance of a garden (garden)

            Args:
                garden_name (str): Name of the garden
                manager (GardenManager): Who the manager of the garden is
            """
            self.garden_name: str = garden_name
            self.manager: GardenManager = manager
            self.plants_list: list[Plant] = []
            self.points: int = 0

        def add_plants(self, plant: Plant) -> None:
            """Adds plants to the garden and updates statistics for the garden

            Args:
                plant (Plant): The plant that needs to be added to the garden
            """
            self.plant: Plant = plant
            self.plants_list.append(self.plant)
            self.manager.manager_stats.plants_added += 1
            if plant.height > 0:
                self.manager.manager_stats.height_validation = True
            print(f"Added {self.plant.name} to "
                  f"{self.garden_name}'s garden")

        def grow(self) -> None:
            """Grows plants in the garden and updates statistics for the garden
            """
            i: int = 0
            nbr_plants: int = len(self.plants_list)
            print(f"\n{self.garden_name} is helping all the plants grow...")
            for i in range(0, nbr_plants):
                self.plants_list[i].height += 1
                print(f"{self.plants_list[i].name} grew 1cm")
            self.manager.manager_stats.total_growth = nbr_plants

    class GardenStats:
        """A class for collecting statistics for the manager on the gardens
        that they manage
        """
        def __init__(self, manager: 'GardenManager'):
            """Creates an instance of the statistics for the garden

            Args:
                manager (GardenManager): The manager we need to collect the
                statistics for
            """
            self.manager: GardenManager = manager
            self.plants_added: int = 0
            self.total_growth: int = 0
            self.height_validation: bool = False
            self.nbr_gardens: int = 0

        @staticmethod
        def count_plant_types(garden: 'GardenManager.Garden') -> list[int]:
            """Counts the number of each type of plant we have in the garden

            Args:
                manager (GardenManager): The manager for the garden we need to
                collect these statistics for

            Returns:
                list[int]: Returns a list with the nbr of plants per type, in
                the order of Plant[0], Flower[1], and PrizedFlower[2]
            """
            nbr_prize_flower: int = 0
            nbr_flower: int = 0
            nbr_plant: int = 0
            count_plant_types: list[int] = []
            for plant in garden.plants_list:
                if isinstance(plant, PrizeFlower):
                    nbr_prize_flower += 1
                elif isinstance(plant, Flower):
                    nbr_flower += 1
                else:
                    nbr_plant += 1
            count_plant_types = [nbr_plant, nbr_flower, nbr_prize_flower]
            return count_plant_types

        def count_gardens(self, manager: 'GardenManager') -> None:
            """Counts the number of gardens that the manager manages

            Args:
                manager (GardenManager): The manager that manages the gardens
            """
            manager.manager_stats.nbr_gardens += len(manager.gardens)

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        """Creates the network of gardens for the manager

        Returns:
            GardenManager: The manager for the grden network
        """
        manager: GardenManager = cls("Manager")
        alice: GardenManager.Garden = manager.Garden("Alice", manager)
        manager.gardens.append(alice)
        bob: GardenManager.Garden = manager.Garden("Bob", manager)
        manager.gardens.append(bob)
        return manager


def add_plants_to_garden(manager: GardenManager, plants: list[Plant]) -> None:
    """Loops through the list of plants I manually added and adds them to
    the garden

    Args:
        manager (GardenManager): Manager for the garden
        plants (list[Plant]): The list of plants I need to add to the garden
    """
    for plant in plants:
        manager.gardens[0].add_plants(plant)


def print_plant(plant: Plant) -> None:
    """Prints the name and height of the plant

    Args:
        plant (Plant): The plant we need to print the information for
    """
    print(f"- {plant.name}: {plant.height}cm")


def print_flower(flower: Flower) -> None:
    """Prints the information for a flower

    Args:
        flower (Flower): The flower we need to print the information for
    """
    if flower.bloom:
        print(f"- {flower.name}: {flower.height}cm"
              f", {flower.colour} flowers"
              f" (blooming)")
    else:
        print(f"- {flower.name}: {flower.height}cm"
              f", {flower.colour} flowers")


def print_prize_flower(prize_flower: PrizeFlower) -> None:
    """Prints information for the prized flower

    Args:
        prize_flower (PrizeFlower): The prized_flower we need to print the
        information for
    """
    if prize_flower.bloom:
        print(f"- {prize_flower.name}: {prize_flower.height}cm"
              f", {prize_flower.colour} flowers"
              f" (blooming), Prize points: {prize_flower.points}")
    else:
        print(f"- {prize_flower.name}: {prize_flower.height}cm"
              f", {prize_flower.colour} flowers")


def garden_report(garden: GardenManager.Garden) -> None:
    """Prints a report for a garden

    Args:
        garden (GardenManager.Garden): The garden I need to print the
        report for
    """
    plant_types: list[int] = []
    print(f"=== {garden.garden_name}'s Garden report ===\n")
    print("Plants in garden:")
    for plant in garden.plants_list:
        if isinstance(plant, PrizeFlower):
            print_prize_flower(plant)
        elif isinstance(plant, Flower):
            print_flower(plant)
        else:
            print_plant(plant)
    print(f"\nPlants added: {garden.manager.manager_stats.plants_added}, "
          f"Total growth: {garden.manager.manager_stats.total_growth}")
    plant_types = garden.manager.manager_stats.\
        count_plant_types(garden)
    print(f"Plant types: {plant_types[0]} "
          f"regular, {plant_types[1]} flowering, "
          f"{plant_types[2]} prize flowers")


def manager_summary(manager: GardenManager) -> None:
    """Prints a summary for the manager

    Args:
        manager (GardenManager): The manager we need to print the
        statistics for
    """
    print(f"\nHeight validation test: "
          f"{manager.manager_stats.height_validation}")
    print(f"Garden scores - {manager.gardens[0].garden_name}: "
          f"{manager.gardens[0].points}, "
          f"{manager.gardens[1].garden_name}: "
          f"{manager.gardens[1].points}")
    manager.manager_stats.count_gardens(manager)
    print(f"Total gardens managed: {manager.manager_stats.nbr_gardens}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    nursery = GardenManager.create_garden_network()

    # Add Plants
    oak_tree: Plant = Plant("Oak Tree", 100)
    rose: Flower = Flower("Rose", 25, "red", True)
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", True, 10)
    plants: list[Plant] = [oak_tree, rose, sunflower]
    add_plants_to_garden(nursery, plants)

    # Grow plants
    nursery.gardens[0].grow()

    # Alice garden report
    print("")
    garden_report(nursery.gardens[0])

    # Manager summary
    nursery.gardens[0].points = 218
    nursery.gardens[1].points = 92
    manager_summary(nursery)
