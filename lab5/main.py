from lab5.shape3d import Cube
from lab5.user_input import get_user_input
from lab5.file_handler import save_to_file
from colorama import init, Fore

# Ініціалізація colorama
init()

def get_color_code(color):
    color_map = {
        'white': Fore.WHITE,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'blue': Fore.BLUE,
        # Додайте більше кольорів за потреби
    }
    return color_map.get(color, Fore.WHITE)  # За замовчуванням білий

def main():
    shape_type, size, color = get_user_input()
    color_code = get_color_code(color)

    if shape_type == 'cube':
        shape = Cube(size, color_code)
        shape.display_ascii_art()
        
        # Додайте можливість масштабування
        scale_option = input("Бажаєте змінити розмір фігури? (yes/no): ")
        if scale_option.lower() == 'yes':
            factor = float(input("Введіть коефіцієнт масштабування: "))
            shape.scale(factor)
            shape.display_ascii_art()
        
        save_option = input("Чи хочете ви зберегти результат у файл? (yes/no): ")
        if save_option.lower() == 'yes':
            filename = input("Введіть ім'я файлу: ")
            save_to_file(filename, shape)
    else:
        print("Невідомий тип фігури.")

if __name__ == "__main__":
    main()