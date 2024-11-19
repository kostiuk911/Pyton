class Calculator:

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

def main():
    calculator = Calculator()
    
    print("Ласкаво просимо до калькулятора!")
    print("Доступні операції:")
    print("1. Додавання (+)")
    print("2. Віднімання (-)")
    print("3. Множення (*)")
    print("4. Ділення (/)")
    while True:
        operation = input("Введіть операцію (або 'exit' для виходу): ").strip()

        if operation == 'exit':
            print("Дякуємо за використання калькулятора!")
            break

        if operation in ['+', '-', '*', '/']:
            try:
                x = float(input("Введіть перше число: "))
                y = float(input("Введіть друге число: "))

                if operation == '+':
                    result = calculator.addition(x, y)
                elif operation == '-':
                    result = calculator.subtraction(x, y)
                elif operation == '*':
                    result = calculator.multiplication(x, y)
                elif operation == '/':
                    result = calculator.division(x, y)

                print(f"Результат: {result}")

            except ValueError as e:
                print(f"Помилка: {e}")
        else:
            print("Невідома операція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()