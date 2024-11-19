class Memory:
    def __init__(self):
        self.value = None

    def save_to_memory(self, result):
        self.value = result
        print(f"Результат {result} збережено в пам'ять.")

    def recall_from_memory(self):
        if self.value is not None:
            print(f"Отримане значення з пам'яті: {self.value}")
            return self.value
        else:
            print("Пам'ять порожня.")
            return None
