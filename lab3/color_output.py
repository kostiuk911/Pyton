from termcolor import colored

# Вибір кольору
def choose_color():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    print("\nДоступні кольори:")
    for i, color in enumerate(colors):
        print(f"{i + 1}. {color}")
    choice = int(input("\nВиберіть колір за номером: ")) - 1
    return colors[choice]

# Виведення ASCII-арту
def print_ascii_art(ascii_art, color):
    print(colored(ascii_art, color))

# Попередній перегляд ASCII-арту
def preview_ascii_art(ascii_art, color):
    print("\nПопередній перегляд вашого ASCII-арту:")
    print_ascii_art(ascii_art, color)
