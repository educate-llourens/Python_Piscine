#!/usr/bin/env python3

# 'pixel_sword': 1, 'code_bow': 1, 'health_byte': 1, '
# quantum_ring': 3}, 'total_value': 1875, 'item_count': 6

def find_least_abundant(inventory: dict[str, int]) -> str:
    min_value: float = float('inf')
    min_key: str = ""

    for name, qty in inventory.items():
        if qty < min_value:
            min_key = name
            min_value = qty
    return min_key


def find_most_abundant(inventory: dict[str, int]) -> str:
    maximum_value: int = -1
    maximum_key: str = ""

    for name, qty in inventory.items():
        if qty > maximum_value:
            maximum_key = name
            maximum_value = qty
    return maximum_key


def inventory_overview(inventory: dict, value_total: int) -> None:
    percentage: float = 0

    for name, qty in inventory.items():
        percentage = qty / value_total * 100
        print(f"{name}: {qty} unit/s ({percentage:.1f}%)")


def find_inventory_total(inventory: dict[str, int]) -> int:
    total: int = 0

    for quantity in inventory.values():
        total += quantity
    return total


def create_dictionary() -> dict[str, int]:
    """Creates the dictionary we need to use
    """
    args: list[str] = []
    split_list: list[str] = []
    item_list: list[tuple[str, int]] = []

    args = ["sword:1", "potion:5", "shield:2", "armor:3", "helmet:1"]
    for i in args:
        split_list = i.split(":")
        try:
            item_list.append((split_list[0], int(split_list[1])))
        except ValueError:
            print("Error: quantity is not a valid number\n")
    return dict(item_list)


def main() -> None:
    inventory: dict[str, int]
    inventory_total: int = 0
    most_abundant: str = ""
    least_abundant: str = ""

    print("=== Inventory System Analysis ===")
    inventory = create_dictionary()
    inventory_total = find_inventory_total(inventory)
    print(f"Total items in inventory: {inventory_total}")
    print(f"Unique item types: {len(inventory)}")
    print("")

    print("=== Current Inventory ===")
    inventory_overview(inventory, inventory_total)
    print("")

    print("=== Inventory Statistics ===")
    most_abundant = find_most_abundant(inventory)
    least_abundant = find_least_abundant(inventory)
    print(f"Most abundant: {most_abundant} ({inventory[most_abundant]} units)")
    print(f"Least abundant: {least_abundant}"
          f"({inventory[least_abundant]} units)")
    print("")

    print("=== Item Categories ===")


if __name__ == "__main__":
    main()
