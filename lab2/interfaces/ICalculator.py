from abc import ABC, abstractmethod

class ICalculator(ABC):
    """
    Абстрактний клас, що визначає інтерфейс калькулятора.
    Кожен підклас повинен реалізувати ці методи.
    """

    @abstractmethod
    def addition(self, x, y):
        pass

    @abstractmethod
    def subtraction(self, x, y):
        pass

    @abstractmethod
    def multiplication(self, x, y):
        pass

    @abstractmethod
    def division(self, x, y):
        pass

    @abstractmethod
    def power(self, x, y):
        pass

    @abstractmethod
    def square_root(self, x):
        pass

    @abstractmethod
    def modulus(self, x, y):
        pass
