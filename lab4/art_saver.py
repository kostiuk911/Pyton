def save_art(art):
    filename = input("Введіть назву файлу для збереження (з розширенням .txt): ")
    with open(filename, 'w', encoding='utf-8') as f:
        for line in art:
            f.write(line + '\n')
    print(f"ASCII-арт збережено у файл {filename}")