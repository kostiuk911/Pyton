import matplotlib.pyplot as plt
from .base_visualizer import BaseVisualizer
from lab8.export_manager import ExportManager

class MultiPlotVisualizer(BaseVisualizer):
    def __init__(self, data):
        super().__init__(data)

    def plot_multiple(self, x_col, y_cols):
        fig, axs = plt.subplots(len(y_cols), 1, figsize=(8, 6))
        for i, y_col in enumerate(y_cols):
            axs[i].plot(self.data[x_col], self.data[y_col])
            axs[i].set_title(f"{x_col} vs {y_col}")
            axs[i].set_xlabel(x_col)
            axs[i].set_ylabel(y_col)
        fig.tight_layout()
        ExportManager.save_plot_as_image("multi_plot.png")
        plt.show()
