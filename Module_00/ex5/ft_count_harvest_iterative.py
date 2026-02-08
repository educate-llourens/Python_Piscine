def ft_count_harvest_iterative() -> None:
    user_input: str = input("Days until harvest: ")
    i: int = 0
    for i in range(0, int(user_input)):
        print(f"Day {i + 1}")
    print("Harvest time!")
