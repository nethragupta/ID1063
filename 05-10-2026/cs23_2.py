# GATE CS 2025 Q.23:  x + k*y = 1,  k*x + y = -1
# Verifies all three cases by row elimination and plots each one.
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")          
import matplotlib.pyplot as plt

EPS = 1e-9

def row_eliminate(k):
    """Reduce [A|b] with R2 -> R2 - k*R1 and classify the system."""
    M = np.array([[1.0, k, 1.0],
                  [k, 1.0, -1.0]])
    M[1] = M[1] - (M[1, 0] / M[0, 0]) * M[0]
    print(f"k = {k:5}: reduced [A|b] =\n{M}")

    if abs(M[1, 1]) < EPS:
        if abs(M[1, 2]) > EPS:
            print(f"  Row 2 says 0 = {M[1, 2]:.2f}  ->  NO SOLUTION\n")
            return "No solution", None
        print("  Row 2 says 0 = 0  ->  INFINITELY MANY SOLUTIONS\n")
        return "Infinitely many solutions", None

    y = M[1, 2] / M[1, 1]
    x = (M[0, 2] - M[0, 1] * y) / M[0, 0]
    print(f"  UNIQUE SOLUTION: x = {x:.4f}, y = {y:.4f}")
    print(f"  Formula check: 1/(1-k) = {1/(1-k):.4f}, -1/(1-k) = {-1/(1-k):.4f}\n")
    return "Unique solution", (x, y)

# One value of k for each case
cases = [(1, "k = 1"), (-1, "k = -1"), (2, "k = 2")]

fig, axes = plt.subplots(3, 1, figsize=(6, 14))
x = np.linspace(-4, 4, 400)

for ax, (k, label) in zip(axes, cases):
    result, point = row_eliminate(k)

    # Line 1: x + k*y = 1  ->  y = (1 - x)/k     (k != 0 here)
    # Line 2: k*x + y = -1 ->  y = -1 - k*x
    y1 = (1 - x) / k
    y2 = -1 - k * x

    ax.plot(x, y1, color="tab:blue", lw=2.5, label=f"x + ({k})y = 1")
    ax.plot(x, y2, color="tab:orange", lw=2.5,
            ls="--" if k == -1 else "-",      # dashed so coincident lines are both visible
            label=f"({k})x + y = -1")

    if point is not None:
        ax.plot(*point, "ro", ms=9, zorder=5)
        ax.annotate(f"({point[0]:.0f}, {point[1]:.0f})", point,
                    textcoords="offset points", xytext=(10, 10), fontsize=11)

    ax.set_title(f"{label}: {result}", fontsize=13)
    ax.axhline(0, color="gray", lw=0.6)
    ax.axvline(0, color="gray", lw=0.6)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-5, 5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right")

plt.tight_layout()
out_file = "three_cases.pdf"
plt.savefig(out_file)
plt.close(fig)
print(f"Saved plot to {os.path.abspath(out_file)}")

# Open the PDF in Android's default PDF viewer (termux-open comes with Termux)
os.system(f"termux-open {out_file}")

