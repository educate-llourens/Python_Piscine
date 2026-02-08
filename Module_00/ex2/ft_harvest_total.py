def ft_harvest_total() -> None:
    i: int = 0
    weight: int = 0
    while i < 3:
        user_input: str = input(f"Day {i + 1} harvest: ")
        weight += int(user_input)
        i += 1
    print(f"Total harvest: {weight}")
