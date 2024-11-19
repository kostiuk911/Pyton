def get_user_input():
    shape_type = input("Введіть тип фігури (cube): ")
    size = int(input("Введіть розмір фігури: "))
    color = input("Введіть колір фігури (white, red, green, blue): ").lower()
    return shape_type, size, color