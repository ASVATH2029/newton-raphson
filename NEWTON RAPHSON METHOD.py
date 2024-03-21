import tkinter as tk

def newton_raphson(func, x, tolerance=1e-6, max_iterations=100):
    for _ in range(max_iterations):
        dx = (func(x + 1e-6) - func(x)) / 1e-6  # Numerical approximation of the derivative
        x -= func(x) / dx
        if abs(func(x)) < tolerance:
            return x
    return None

def find_root():
    try:
        # Get inputs from the entry widgets
        func = lambda x: eval(entry_func.get())
        initial_guess = float(entry_initial_guess.get())
        tolerance = float(entry_tolerance.get())
        max_iterations = int(entry_max_iterations.get())

        # Perform Newton-Raphson method
        root = newton_raphson(func, initial_guess, tolerance, max_iterations)

        if root is not None:
            result_label.config(text=f"Approximate root: {root}")
        else:
            result_label.config(text="Newton-Raphson method did not converge.")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Newton-Raphson Method")

# Function entry
label_func = tk.Label(root, text="Enter the function f(x):")
label_func.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_func = tk.Entry(root, width=30)
entry_func.grid(row=0, column=1, padx=5, pady=5)

# Initial guess entry
label_initial_guess = tk.Label(root, text="Enter the initial guess:")
label_initial_guess.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_initial_guess = tk.Entry(root)
entry_initial_guess.grid(row=1, column=1, padx=5, pady=5)

# Tolerance entry
label_tolerance = tk.Label(root, text="Enter the tolerance:")
label_tolerance.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_tolerance = tk.Entry(root)
entry_tolerance.grid(row=2, column=1, padx=5, pady=5)

# Maximum iterations entry
label_max_iterations = tk.Label(root, text="Enter the maximum number of iterations:")
label_max_iterations.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_max_iterations = tk.Entry(root)
entry_max_iterations.grid(row=3, column=1, padx=5, pady=5)

# Button to find the root
find_button = tk.Button(root, text="Find Root", command=find_root)
find_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Start the GUI
root.mainloop()
