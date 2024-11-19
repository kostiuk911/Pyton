import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def modulus(a, b):
    return a % b