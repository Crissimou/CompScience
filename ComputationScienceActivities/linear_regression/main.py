import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Manual Linear Regression
def linear_regression(x, y):
    # Number of observations
    n = len(x)

    # Calculate the mean of x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Calculate the slope (m) and intercept (b) using the least squares method
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sum((x - mean_x) ** 2)

    m = numerator / denominator
    b = mean_y - m * mean_x

    return m, b

# Predict function
def predict(x, m, b):
    return m * x + b

# Function to perform linear regression and plot the graph
def perform_regression():
    try:
        # Get user inputs
        x_input = entry_x.get()
        y_input = entry_y.get()

        # Convert inputs to numpy arrays
        x = np.array([float(i) for i in x_input.split(',')])
        y = np.array([float(i) for i in y_input.split(',')])

        # Perform linear regression
        m, b = linear_regression(x, y)

        # Predict y values
        y_pred = predict(x, m, b)

        # Update the slope and intercept labels
        slope_label.config(text=f"Slope (m): {m:.4f}")
        intercept_label.config(text=f"Intercept (b): {b:.4f}")

        # Create a scatter plot with the regression line using seaborn
        sns.set(style="whitegrid")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x=x, y=y, color='blue', label='Data points', ax=ax)
        sns.lineplot(x=x, y=y_pred, color='red', label='Regression line', ax=ax)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Linear Regression with Seaborn')
        ax.legend()

        # Clear any previous plot
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Display the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        # Show error message if something goes wrong
        slope_label.config(text="Error")
        intercept_label.config(text=str(e))

# Create the main window
window = tk.Tk()
window.title("Linear Regression")

# Create and place labels and entry widgets
label_x = tk.Label(window, text="Enter X values (comma-separated):")
label_x.grid(row=0, column=0, padx=10, pady=10)

entry_x = tk.Entry(window, width=50)
entry_x.grid(row=0, column=1, padx=10, pady=10)

label_y = tk.Label(window, text="Enter Y values (comma-separated):")
label_y.grid(row=1, column=0, padx=10, pady=10)

entry_y = tk.Entry(window, width=50)
entry_y.grid(row=1, column=1, padx=10, pady=10)

# Create and place the button to perform regression
button = tk.Button(window, text="Perform Regression", command=perform_regression)
button.grid(row=2, column=0, columnspan=2, pady=10)

# Create labels to display slope and intercept
slope_label = tk.Label(window, text="Slope (m): ")
slope_label.grid(row=3, column=0, columnspan=2, pady=5)

intercept_label = tk.Label(window, text="Intercept (b): ")
intercept_label.grid(row=4, column=0, columnspan=2, pady=5)

# Create a frame to hold the plot
plot_frame = tk.Frame(window)
plot_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()