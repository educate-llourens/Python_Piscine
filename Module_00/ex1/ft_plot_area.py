def ft_plot_area() -> None:
    user_length: str = input("Enter length: ")
    len: int = int(user_length)
    user_width: str = input("Enter width: ")
    width: int = int(user_width)
    area = len * width
    print(f"Plot area: {area}")
