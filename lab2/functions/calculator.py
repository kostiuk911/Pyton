import math
from lab2.functions.memory import Memory
from lab2.functions.history import History
from lab2.functions.settings import AppSettings

class Calculator:
    def __init__(self):
        self.memory = Memory()
        self.history = History()
        self.settings = AppSettings()

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y == 0:
            return "Помилка: ділення на нуль"
        return x / y

    def power(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            return "Помилка: квадратний корінь з від'ємного числа"
        return math.sqrt(x)

    def modulus(self, x, y):
        return x % y

    def valid_operator(self, operator):
        return operator in ['+', '-', '*', '/', '^', '√', '%']

    
    def run_calculator(self):
     while True:
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")

            while not self.valid_operator(operator):
                print("Невірний оператор. Спробуйте ще раз.")
                operator = input("Введіть дійсний оператор (+, -, *, /, ^, √, %): ")

            if operator == '√':
                result = self.square_root(num1)
                expression = f"√{num1}"
            else:
                num2 = float(input("Введіть друге число: "))
                result = self.perform_operation(num1, num2, operator)
                expression = f"{num1} {operator} {num2}"

        except ValueError:
            print("Невірне значення. Будь ласка, введіть число.")
            continue

        print(f"Результат: {result:.{self.settings.decimal_places}f}")
        self.history.add_to_history(expression, result)

        if self.settings.memory_enabled:
            self.memory.save_to_memory(result)

        next_step = input("Хочете отримати значення з пам'яті (м), переглянути історію (іст) або завершити (ні)? ").strip().lower()
        if next_step == 'м':
            self.memory.recall_from_memory()
        elif next_step == 'іст':
            self.history.show_history()
        elif next_step == 'ні':
            pass  # Продовжити до запитання про наступне обчислення

        continue_calculating = input("Бажаєте виконати ще одне обчислення? (так/ні): ").strip().lower()
        if continue_calculating != 'так':
            break



    def perform_operation(self, num1, num2, operator):
        if operator == '+':
            return self.addition(num1, num2)
        elif operator == '-':
            return self.subtraction(num1, num2)
        elif operator == '*':
            return self.multiplication(num1, num2)
        elif operator == '/':
            return self.division(num1, num2)
        elif operator == '^':
            return self.power(num1, num2)
        elif operator == '%':
            return self.modulus(num1, num2)
