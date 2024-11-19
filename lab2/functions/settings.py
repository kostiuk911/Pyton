class AppSettings:
    def __init__(self):
        self.decimal_places = 2  
        self.memory_enabled = False  # За замовчуванням вимкнена
        self.configure_settings()

    def configure_settings(self):
        while True:
            try:
                self.decimal_places = int(input("Введіть кількість десяткових розрядів (0-10): "))
                if 0 <= self.decimal_places <= 10:
                    break
                else:
                    print("Будь ласка, введіть число в межах від 0 до 10.")
            except ValueError:
                print("Невірне значення. Спробуйте ще раз.")

        while True:
            memory_option = input("Включити функцію пам'яті? (так/ні): ").strip().lower()
            if memory_option in ['так', 'ні']:
                self.memory_enabled = memory_option == 'так'
                if self.memory_enabled:
                    print("Функція пам'яті увімкнена.")
                else:
                    print("Функція пам'яті вимкнена.")
                break
            else:
                print("Будь ласка, введіть 'так' або 'ні'.")
