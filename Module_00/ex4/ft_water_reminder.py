def ft_water_reminder() -> None:
    user_input: str = input("Days since last watering: ")
    if int(user_input) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
