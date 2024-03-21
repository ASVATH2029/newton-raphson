def newton_raphson(func, x, tolerance=1e-6, max_iterations=100):
    for _ in range(max_iterations):
        dx = (func(x + 1e-6) - func(x)) / 1e-6  # Numerical approximation of the derivative
        x -= func(x) / dx
        if abs(func(x)) < tolerance:
            return x
    return None

# Example usage:
def f(x):
    return 2*x**3 - 3*x - 6

initial_guess = 2.0
root = newton_raphson(f, initial_guess)

if root is not None:
    print("Approximate root:", root)
else:
    print("Newton-Raphson method did not converge.")