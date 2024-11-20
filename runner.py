import sys
import unittest
import logging
from lab1.main import main as lab1_main
from lab2.main import main as lab2_main
from lab3.main import main as lab3_main
from lab4.main import main as lab4_main
from lab5.main import main as lab5_main
from lab7.main import main as lab7_main
from lab8.main import main as lab8_main

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, 
    filename="runner.log", 
    filemode="a", 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RunnerFacade:
    """
    Facade class to manage the execution of all laboratory works.
    """

    def __init__(self):
        # Словник з номером лабораторної роботи та відповідною функцією для запуску
        self.labs = {
            1: lab1_main,
            2: lab2_main,
            3: lab3_main,
            4: lab4_main,
            5: lab5_main,
            6: self.run_lab6_tests,
            7: lab7_main,
            8: lab8_main,
        }
        logging.info("RunnerFacade initialized with labs: %s", list(self.labs.keys()))

    def run_lab(self, lab_number):
        """
        Запускає лабораторну роботу за її номером.
        """
        logging.info("Attempting to run lab %d", lab_number)

        if lab_number in self.labs:
            print(f"\nЗапуск лабораторної роботи {lab_number}...\n")
            try:
                self.labs[lab_number]()  # Виклик функції main() для відповідного модуля
                logging.info("Lab %d completed successfully.", lab_number)
            except Exception as e:
                logging.error("Error while running lab %d: %s", lab_number, str(e))
                print(f"Помилка під час виконання лабораторної роботи {lab_number}: {e}")
        else:
            logging.warning("Lab %d not found.", lab_number)
            print(f"Лабораторна робота {lab_number} не знайдена.")

    @staticmethod
    def run_lab6_tests():
        """
        Запуск юніт-тестів для Лабораторної роботи 6.
        """
        logging.info("Running unit tests for Lab 6")
        print("\nЗапуск юніт-тестів для Лабораторної роботи 6...\n")
        try:
            # Вказуємо шлях до тестового файлу для Lab6
            tests = unittest.defaultTestLoader.discover('lab6', pattern='test_*.py')
            runner = unittest.TextTestRunner()
            result = runner.run(tests)

            # Логування результатів
            if result.wasSuccessful():
                logging.info("All unit tests for Lab 6 passed.")
            else:
                logging.warning(
                    "Some unit tests for Lab 6 failed. Failures: %d, Errors: %d",
                    len(result.failures), len(result.errors)
                )
        except Exception as e:
            logging.error("Error while running unit tests for Lab 6: %s", str(e))
            print(f"Помилка під час виконання юніт-тестів: {e}")


def display_menu():
    """
    Display a menu for selecting the laboratory work to run.
    """
    print("\n=== Laboratory Work Runner ===")
    print("1. Run Lab 1")
    print("2. Run Lab 2")
    print("3. Run Lab 3")
    print("4. Run Lab 4")
    print("5. Run Lab 5")
    print("6. Run Lab 6 (Unit Tests)")
    print("7. Run Lab 7")
    print("8. Run Lab 8")
    print("0. Exit")


def main():
    """
    Main function to handle user input and invoke the corresponding lab work.
    """
    runner = RunnerFacade()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                logging.info("Exiting the program.")
                print("Exiting the program.")
                sys.exit(0)
            else:
                runner.run_lab(choice)
        else:
            logging.warning("Invalid input: %s", choice)
            print("Invalid input! Please enter a number from the menu.")


if __name__ == "__main__":
    main()
