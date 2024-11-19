def getUserInput():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /, ^, √, %): ")
        return num1, num2, operator
    except ValueError:
        return "Error: Invalid input", None, None