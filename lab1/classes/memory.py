class Memory:
    def __init__(self):
        self.memory = None

    def store(self, value):
        self.memory = value

    def recall(self):
        return self.memory

    def clear(self):
        self.memory = None