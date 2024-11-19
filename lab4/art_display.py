import os

def display_art(art):
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in art:
        print(line)

def preview_art(art):
    print("Попередній перегляд ASCII-арту:")
    display_art(art)
    input("Натисніть Enter, щоб продовжити...")