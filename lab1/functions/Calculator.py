import math

class Calculator:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.operator = ''
        self.valid_operators = ['+', '-', '*', '/', '^', '√', '%']

    def get_user_input(self):
        expression = input("Enter expression (e.g. '5 + 3' or '√9'): ").strip()
        return self.parse_expression(expression)

    def parse_expression(self, expression):
        if '√' in expression:
            self.operator = '√'
            self.num1 = float(expression[1:])
            self.num2 = None
        else:
            for operator in self.valid_operators:
                if operator in expression:
                    self.num1, self.num2 = map(float, expression.split(operator))
                    self.operator = operator
                    break
        if self.operator not in self.valid_operators:
            raise ValueError("Invalid operator!")

    def check_operator(self):
        if self.operator not in self.valid_operators:
            raise ValueError(f"Invalid operator: {self.operator}")

    def calculate(self):
        try:
            if self.operator == '+':
                return self.num1 + self.num2
            elif self.operator == '-':
                return self.num1 - self.num2
            elif self.operator == '*':
                return self.num1 * self.num2
            elif self.operator == '/':
                if self.num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero!")
                return self.num1 / self.num2
            elif self.operator == '^':
                return self.num1 ** self.num2
            elif self.operator == '√':
                if self.num1 < 0:
                    raise ValueError("Cannot take square root of negative number!")
                return math.sqrt(self.num1)
            elif self.operator == '%':
                return self.num1 % self.num2
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            return None

    def display_result(self, result):
        if result is not None:
            print(f"Result: {result:.2f}")
        else:
            print("Error occurred during calculation.")

    def run(self):
        while True:
            try:
                self.get_user_input()
                result = self.calculate()
                self.display_result(result)
            except ValueError as e:
                print(e)
            
            choice = input("Do you want to perform another calculation? (y/n): ").lower()
            if choice != 'y':
                break