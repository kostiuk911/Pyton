import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self._file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self._file_path)
        print("Data loaded successfully.")
        return self.data

    def get_extremes(self):
        # Визначення екстремальних значень для всіх числових стовпців
        return self.data.describe()
