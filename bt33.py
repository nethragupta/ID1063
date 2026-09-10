import numpy as np
import matplotlib.pyplot as plt
import os
# Define the function and its derivative
def f(x):
    return np.exp(x) - 2

def df(x):
    return np.exp(x)

# Newton-Raphson implementation
def newton_raphson(x0, iterations=1):
    x = x0
    for _ in range(iterations):
        x = x - f(x) / df(x)
    return x

# Given initial guess
x0 = 1.0

# Calculate root after 1 iteration (as requested in the question)
x1 = newton_raphson(x0, iterations=1)
print(f"Approximated value after 1 iteration: {x1:.2f}")

# Calculate true root (ln(2))
exact_root = np.log(2)
print(f"Exact root: {exact_root:.4f}")

# --- Plotting the graph ---
x_vals = np.linspace(-0.5, 1.5, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r'$f(x) = e^x - 2$', color='blue', linewidth=2)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  # x-axis
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)  # y-axis

# Mark the points
plt.plot(x0, f(x0), 'ro', label=f'Initial Guess $x_0 = {x0}$')
plt.plot(x1, 0, 'go', label=f'1st Iteration $x_1 = {x1:.2f}$')
plt.plot(exact_root, 0, 'kx', markersize=8, label=f'Exact Root $\\approx {exact_root:.2f}$')

# Tangent line at x0 = 1
tangent_y = f(x0) + df(x0) * (x_vals - x0)
plt.plot(x_vals, tangent_y, 'r--', alpha=0.6, label='Tangent line at $x_0$')

plt.ylim(-2.5, 3)
plt.title("Newton-Raphson Method for $e^x - 2 = 0$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
#plt.savefig('/sdcard/Download/bt331.jpg')
# Save the plot image
plt.savefig("plot.pdf", bbox_inches="tight", dpi=300)
os.system("termux-open plot.pdf")
print("Plot saved as plot.pdf")

