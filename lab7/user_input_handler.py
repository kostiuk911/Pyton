class UserInputHandler:
    """Клас для обробки введення користувача"""

    def get_user_choice(self):
        print("1. Показати всі дані (таблиця)")
        print("2. Показати дані у форматі списку")
        print("3. Зберегти дані")
        return input("Виберіть опцію: ")

    def validate_choice(self, choice):
        return choice in ["1", "2", "3"]
