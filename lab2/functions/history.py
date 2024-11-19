class History:
    def __init__(self):
        self.history = []

    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result:.{2}f}")

    def show_history(self):
        if self.history:
            print("Історія обчислень:")
            for entry in self.history:
                print(entry)
        else:
            print("Історія порожня.")
