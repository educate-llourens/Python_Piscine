#!/usr/bin/env python3

import sys


def find_item(dictionary: dict) -> bool:
    players: dict = {}
    alice: dict = {}
    alice_items: dict = {}

    players = dictionary.get("players", {})
    alice = players.get("alice", {})
    alice_items = alice.get("items", {})
    if alice_items.get("sword") is not None:
        return True
    return False


def get_values(dictionary: dict) -> list[int]:
    players: dict = {}
    alice: dict = {}
    alice_items: dict = {}
    values: list[int] = []

    players = dictionary.get("players", {})
    alice = players.get("alice", {})
    alice_items = alice.get("items", {})
    for value in alice_items.values():
        values.append(value)
    return values


def get_keys(dictionary: dict) -> list[str]:
    players: dict = {}
    alice: dict = {}
    alice_items: dict = {}
    keys: list[str] = []

    players = dictionary.get("players", {})
    alice = players.get("alice", {})
    alice_items = alice.get("items", {})
    for key in alice_items.keys():
        keys.append(key)
    return keys


def find_common_items(dictionary: dict) -> dict:
    players: dict = {}
    alice: dict = {}
    alice_items: dict = {}
    catalogue: dict = {}
    common_items: dict = {}
    item_reference: dict = {}
    item_rarity: str = ""

    players = dictionary.get("players", {})
    alice = players.get("alice", {})
    alice_items = alice.get("items", {})
    catalogue = dictionary.get("catalogue", {})

    for item_name, qty in alice_items.items():
        item_reference = catalogue.get(item_name, {})
        item_rarity = item_reference.get("rarity", "")
        if item_rarity == "common":
            common_items.update({item_name: qty})
    return common_items


def find_rarest_items(dictionary: dict) -> dict:
    players: dict = {}
    alice: dict = {}
    alice_items: dict = {}
    catalogue: dict = {}
    rare_items: dict = {}
    item_reference: dict = {}
    item_rarity: str = ""

    players = dictionary.get("players", {})
    alice = players.get("alice", {})
    alice_items = alice.get("items", {})
    catalogue = dictionary.get("catalogue", {})

    for item_name, qty in alice_items.items():
        item_reference = catalogue.get(item_name, {})
        item_rarity = item_reference.get("rarity", "")
        if item_rarity == "legendary" or item_rarity == "rare":
            rare_items.update({item_name: qty})
    return rare_items


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
    players: dict = dictionary.get("players", {})
    alice = players.get("alice", {})
    return alice


def update_item_count(alice: dict) -> None:
    new_item_count: int = 0
    alice_items: dict = {}

    alice_items = alice.get("items", {})
    for qty in alice_items.values():
        new_item_count += qty
    alice.update({"item_count": new_item_count})


def update_dictionary(dictionary: dict) -> dict:
    updated_items: dict = {"items": {}}
    split_list: list[str] = []
    name: str = ""
    qty: int = 0
    players: dict
    alice: dict

    for item in sys.argv[1:]:
        split_list = item.split(":")
        if len(split_list) != 2:
            print(f"Error: Invalid usage: '{item}'. Expected 'name:qty")
            return dictionary
        name = split_list[0]
        try:
            qty = int(split_list[1])
            updated_items["items"][name] = qty
        except ValueError:
            print("Error: Could not convert argv value to int")
            continue
        except IndexError as msg:
            print(f"Error: {msg}")
            continue
    players = dictionary.get("players", {})
    alice = players.get("alice", {})
    alice["items"] = updated_items["items"]
    update_item_count(alice)
    return dictionary


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
            "sword": {
                'type': 'weapon',
                'value': 150,
                'rarity': 'common'
            },
            'armor': {
                'type': 'accessory',
                'value': 500,
                'rarity': 'rare'
            },
            'potion': {
                'type': 'consumable',
                'value': 25,
                'rarity': 'common'
            },
            'data_crystal': {
                'type': 'material',
                'value': 1000,
                'rarity': 'legendary'
            },
            'bow': {
                'type': 'weapon',
                'value': 200,
                'rarity': 'uncommon'
            },
        },
    }
    return inventory


def main() -> None:
    dictionary: dict = {}
    inventory: dict = {}
    inventory_total: int = 0
    most_abundant: tuple[str, int]
    least_abundant: tuple[str, int]
    rarest_items: dict = {}
    common_items: dict = {}

    if len(sys.argv[1:]) < 1:
        print("Error: Not enough argumants. Usage: ./program_name "
              "item:value item:value")
        return
    dictionary = create_dictionary()
    if len(sys.argv[1:]) >= 2:
        dictionary = update_dictionary(dictionary)
    inventory = get_inventory(dictionary)

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
    rarest_items = find_rarest_items(dictionary)
    common_items = find_common_items(dictionary)
    print(f"Rare: {rarest_items}")
    print(f"Common: {common_items}")
    print("")

    print("=== Management Suggestions ===")
    restock_items: list[str] = find_restock(inventory)
    print(f"Restock needed: {restock_items}")
    print("")

    print("=== Dictionary Properties Demo ===")
    keys: list[str] = get_keys(dictionary)
    values: list[int] = get_values(dictionary)
    print("Dictionary keys:", end="")
    for key in keys:
        print(f" {key}", end=",")
    print("\nDictionary values:", end="")
    for value in values:
        print(f" {value}", end=",")
    print(f"\nSample lookup - 'sword' in inventory: {find_item(dictionary)}")


if __name__ == "__main__":
    main()
