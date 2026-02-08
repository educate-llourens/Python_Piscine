def ft_count_harvest_recursive() -> None:
    def recursion(current_day, last_day) -> None:
        if current_day <= last_day:
            print(f"Day {current_day}")
            recursion(current_day + 1, last_day)

    user_input: str = input("Days until harvest: ")
    last_day = int(user_input)
    recursion(1, last_day)
    print("Harvest time!")
