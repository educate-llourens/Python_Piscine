def ft_seed_inventory(produce: str, amount: int, metric: str) -> None:
    if metric == "packets":
        print(f"{produce.capitalize()} seeds: {amount} {metric} available")
    elif metric == "grams":
        print(f"{produce.capitalize()} seeds: {amount} {metric} total")
    elif metric == "area":
        print(f"{produce.capitalize()} seeds: covers {amount} square meters")
    else:
        print("Unknown unit type")
