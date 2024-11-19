import requests
import logging

# Налаштування URL API
API_URL = "https://jsonplaceholder.typicode.com/posts"  # JSON Placeholder API

class APIHandler:
    """Клас для роботи з API"""

    def fetch_data(self):
        """Метод для отримання даних з API"""
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()
            logging.info("Дані успішно отримані.")
            return data
        except requests.exceptions.RequestException as e:
            logging.error(f"Помилка API: {e}")
            print(f"Помилка API: {e}")
            return None
