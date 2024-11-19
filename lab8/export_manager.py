import os
import matplotlib.pyplot as plt

class ExportManager:
    @staticmethod
    def save_plot_as_image(filename):
        # Define the directory to save images
        output_dir = "output_images"
        os.makedirs(output_dir, exist_ok=True)  # Create folder if it doesn't exist

        # Full path for the image file
        filepath = os.path.join(output_dir, filename)
        
        # Save the plot to the specified directory
        plt.savefig(filepath)
        print(f"Saved plot as {filepath}")
