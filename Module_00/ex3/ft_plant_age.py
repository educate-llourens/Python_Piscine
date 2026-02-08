def ft_plant_age() -> None:
    user_input: str = input("Enter plant age in days: ")
    if int(user_input) > 60:
        print("Plant is ready to harvest!")
    elif int(user_input) <= 60:
        print("Plant needs more time to grow.")
