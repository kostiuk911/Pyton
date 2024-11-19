from lab3.user_input import get_user_input
from lab3.ascii_art import generate_ascii_art, choose_font, resize_ascii_art, replace_characters
from lab3.color_output import choose_color, print_ascii_art, preview_ascii_art
from lab3.file_operations import save_to_file

def main():
    # Введення користувача
    text = get_user_input()
    
    # Вибір шрифту
    font = choose_font()
    
    # Генерація ASCII-арту
    ascii_art = generate_ascii_art(text, font)
    
    # Вибір кольору
    color = choose_color()

    # Попередній перегляд
    preview_ascii_art(ascii_art, color)

    while True:
        print("\nЩо ви хочете зробити далі?")
        print("1. Змінити розмір ASCII-арту")
        print("2. Замінити символи в ASCII-арті")
        print("3. Вивести ASCII-арт")
        print("4. Зберегти ASCII-арт у файл")
        print("5. Вийти")

        choice = input("Виберіть опцію (1-5): ")

        if choice == '1':
            # Масштабування
            width = int(input("Введіть ширину: "))
            ascii_art = resize_ascii_art(text, font, width)
            preview_ascii_art(ascii_art, color)
        
        elif choice == '2':
            # Заміна символів
            old_char = input("Введіть символ, який хочете замінити: ")
            new_char = input("Введіть новий символ: ")
            ascii_art = replace_characters(ascii_art, old_char, new_char)
            preview_ascii_art(ascii_art, color)
        
        elif choice == '3':
            # Виведення ASCII-арту
            print_ascii_art(ascii_art, color)
        
        elif choice == '4':
            # Збереження у файл
            save_to_file(ascii_art)
        
        elif choice == '5':
            # Вихід з програми
            print("Дякуємо за використання програми!")
            break
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
