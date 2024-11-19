import matplotlib.pyplot as plt
from .base_visualizer import BaseVisualizer
from lab8.export_manager import ExportManager

class BarChartVisualizer(BaseVisualizer):
    def __init__(self, data, x_col, y_col):
        super().__init__(data)
        self.x_col = x_col
        self.y_col = y_col

    def plot(self):
        plt.bar(self.data[self.x_col], self.data[self.y_col], label=f"{self.x_col} vs {self.y_col}")
        plt.xlabel(self.x_col)
        plt.ylabel(self.y_col)
        plt.title("Bar Chart")
        plt.legend()
        ExportManager.save_plot_as_image("bar_chart.png")
        plt.show()
