def get_user_input():
    text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")
    
    while True:
        try:
            width = int(input("Введіть ширину ASCII-арту (макс. 100): "))
            if 1 <= width <= 100:
                break
            else:
                print("Будь ласка, введіть число від 1 до 100.")
        except ValueError:
            print("Будь ласка, введіть коректне число.")
    
    while True:
        try:
            height = int(input("Введіть висоту ASCII-арту (макс. 30): "))
            if 1 <= height <= 30:
                break
            else:
                print("Будь ласка, введіть число від 1 до 30.")
        except ValueError:
            print("Будь ласка, введіть коректне число.")
    
    alignment = input("Виберіть вирівнювання (left, center, right): ").strip().lower()
    while alignment not in ['left', 'center', 'right']:
        alignment = input("Невірне вирівнювання. Виберіть (left, center, right): ").strip().lower()
    
    color_option = input("Виберіть колір (black and white, gray): ").strip().lower()
    while color_option not in ['black and white', 'gray']:
        color_option = input("Невірний вибір. Виберіть (black and white, gray): ").strip().lower()
    
    return text, width, height, alignment, color_option