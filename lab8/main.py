from lab8.data_loader import DataLoader
from lab8.visualizers.line_chart import LineChartVisualizer
from lab8.visualizers.bar_chart import BarChartVisualizer
from lab8.visualizers.multi_plot import MultiPlotVisualizer

def main():
        # Load data
    data_loader = DataLoader("lab8/data.csv")
    data = data_loader.load_data()

    # Display data extremes
    print("Data extremes:\n", data_loader.get_extremes())

    # Plot line chart
    line_chart = LineChartVisualizer(data, x_col="Date", y_col="Value")
    line_chart.plot()

    # Plot bar chart
    bar_chart = BarChartVisualizer(data, x_col="Category", y_col="Date")
    bar_chart.plot()

    # Plot multi-plot
    multi_plot = MultiPlotVisualizer(data)
    multi_plot.plot_multiple(x_col="Date", y_cols=["Value", "Category"])
if __name__ == "__main__":
    main ()
