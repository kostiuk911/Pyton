from tabulate import tabulate
import json
from colorama import Fore, Style

class DataVisualizer:
    """Клас для візуалізації даних"""

    def display_data(self, data, display_type="table"):
        """Відображення даних у табличному або списковому форматі"""
        if display_type == "table":
            print(Fore.BLUE + Style.BRIGHT + tabulate(data, headers="keys", tablefmt="grid") + Style.RESET_ALL)
        elif display_type == "list":
            for item in data:
                print(Fore.GREEN + json.dumps(item, indent=4) + Style.RESET_ALL)
