#!/usr/bin/env python3

def append_str(str_list: list[str], string: str) -> list[str]:
    """Appends a string to a list of strings

    Args:
        str_list (list[str]): The list we need to append to
        string (str): The string we need to append

    Returns:
        list[str]: Returns an updated list of strings
    """
    new_list: list[str] = []

    if not str_list:
        new_list += [string]
        return new_list

    for item in str_list:
        new_list += [item]
    new_list += [string]
    return new_list


def find_restock(inventory: dict) -> list[str]:
    items: dict = inventory.get("items", {})
    restock: list[str] = []

    for name, qty in items.items():
        if qty <= 1:
            restock = append_str(restock, name)
    return restock


def find_least_abundant(inventory: dict) -> tuple[str, int]:
    min_value: float = float('inf')
    min_key: str = ""
    items: dict = inventory.get("items", {})

    for name, qty in items.items():
        if qty < min_value:
            min_key = name
            min_value = qty
    return min_key, int(min_value)


def find_most_abundant(inventory: dict) -> tuple[str, int]:
    maximum_value: int = -1
    maximum_key: str = ""
    items: dict = inventory.get("items", {})

    for name, qty in items.items():
        if qty > maximum_value:
            maximum_key = name
            maximum_value = qty
    return maximum_key, maximum_value


def inventory_overview(inventory: dict, value_total: int) -> None:
    percentage: float = 0
    items: dict = inventory.get("items", {})
    qty: int = 0
    name: str = ""

    for name, qty in items.items():
        percentage = qty / value_total * 100
        print(f"{name}: {qty} unit/s ({percentage:.1f}%)")


def find_inventory_total(inventory: dict) -> int:
    alice_total: int = inventory.get("item_count", 0)
    return alice_total


def get_inventory(dictionary: dict) -> dict:
    players: list[dict, {}] = dictionary.get("players", {})
    alice = players.get("alice", {})
    return alice


def create_dictionary() -> dict:
    """Creates the dictionary we need to use
    """
    inventory = {
        "players": {
            "alice": {
                "items": {
                    'pixel_sword': 1,
                    'code_bow': 1,
                    'health_byte': 1,
                    'quantum_ring': 3
                },
                "total_value": 1875,
                "item_count": 6,
            },
            "charlie": {
                "items": {
                    'pixel_sword': 1,
                    'code_bow': 1
                },
                "total_value": 350,
                "item_count": 2,
            },
            "diana": {
                "items": {
                    'code_bow': 3,
                    'pixel_sword': 3,
                    'health_byte': 3,
                    'data_crystal': 3
                },
                "total_value": 4125,
                "item_count": 12,
            }
        },
        "catalogue": {
            "pixel_sword": {
                'type': 'weapon',
                'value': 150,
                'rarity': 'common'
            },
            'quantum_ring': {
                'type': 'accessory',
                'value': 500,
                'rarity': 'rare'
            },
            'health_byte': {
                'type': 'consumable',
                'value': 25,
                'rarity': 'common'
            },
            'data_crystal': {
                'type': 'material',
                'value': 1000,
                'rarity': 'legendary'
            },
            'code_bow': {
                'type': 'weapon',
                'value': 200,
                'rarity': 'uncommon'
            },
        },
    }
    return inventory


def main() -> None:
    dictionary: dict = create_dictionary()
    inventory: dict = get_inventory(dictionary)
    catalogue: dict = dictionary.get("catalogue", {})
    inventory_total: int = 0
    most_abundant: tuple[str, int]
    least_abundant: tuple[str, int]

    print("=== Inventory System Analysis ===")
    inventory_total = find_inventory_total(inventory)
    total_unique_items = len(inventory.get("items", {}))

    print(f"Total items in inventory: {inventory_total}")
    print(f"Unique item types: {total_unique_items}")
    print("")

    print("=== Current Inventory ===")
    inventory_overview(inventory, inventory_total)
    print("")

    print("=== Inventory Statistics ===")
    most_abundant = find_most_abundant(inventory)
    least_abundant = find_least_abundant(inventory)

    print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")
    print(f"Least abundant: {least_abundant[0]}"
          f"({least_abundant[1]} units)")
    print("")

    print("=== Item Categories ===")
    print("")

    print("=== Management Suggestions ===")
    restock_items: list[str] = find_restock(inventory)
    print(f"Restock needed: {restock_items}")

if __name__ == "__main__":
    main()
