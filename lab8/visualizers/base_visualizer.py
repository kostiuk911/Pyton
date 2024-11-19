import matplotlib.pyplot as plt

class BaseVisualizer:
    def __init__(self, data):
        self.data = data

    def plot(self):
        raise NotImplementedError("Subclasses should implement this method")
