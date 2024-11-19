# Збереження ASCII-арту у файл
def save_to_file(ascii_art):
    filename = "./test.txt"  # Вказуємо шлях без input()
    with open(filename, 'w') as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файл {filename}")
