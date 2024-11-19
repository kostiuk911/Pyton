from lab1.functions.calcFunctions import add, subtract, multiply, divide, power, sqrt, modulus

from lab1.init import memory, app_settings
import lab1.constants.constants as const

history = []

def logToFile(expression, result):
    with open("lab1/logs/calculator_history.txt", "a") as logFile:
        logFile.write(f"{expression} = {result}\n")

def displayHistory():
    if history:
        print("\n--- Calculation History ---")
        for record in history:
            print(record)
    else:
        print("No history available.")

def parse_expression(expression):
    try:
        expression = expression.replace(' ', '')
        if '√' in expression: 
            num = float(expression[1:])
            return num, None, '√'
        for operator in const.VALID_OPERATORS:
            if operator in expression:
                num1, num2 = expression.split(operator)
                return float(num1), float(num2), operator
    except ValueError:
        raise ValueError("Invalid expression format")

def main():
    while True:
        print("\nTo view calculation history, type 'history'")
        userInput = input("Enter an expression (e.g., '5 + 3' or 'exit' to quit): ")

        if userInput.lower() == "history":
            displayHistory()
            continue
        elif userInput.lower() == "exit":
            break

        try:
            num1, num2, operator = parse_expression(userInput)

            if operator not in const.VALID_OPERATORS:
                print("Invalid operator!")
                continue

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '^':
                result = power(num1, num2)
            elif operator == '√':
                result = sqrt(num1)
            elif operator == '%':
                result = modulus(num1, num2)

            expression = f"{num1} {operator} {num2}" if operator != '√' else f"{operator}({num1})"
            result = f"{expression} = {round(result, app_settings.decimal_places)}"

            history.append(result)
            logToFile(expression, result)

            print(result)
            
        except ValueError:
            print("Error: Invalid input.")

        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == '__main__':
    main()