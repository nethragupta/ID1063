import os
import numpy as np
import matplotlib.pyplot as plt

# Conic form: xᵀVx + 2uᵀx + f = 0
# Curve 1: y = x²             →  x² - y = 0
V1 = np.array([[1, 0], [0, 0]]); u1 = np.array([0, -0.5]); f1 = 0
# Curve 2: y = -x² - 2x - 1   →  x² + 2x + y + 1 = 0
V2 = np.array([[1, 0], [0, 0]]); u2 = np.array([1, 0.5]);  f2 = 1

def augmented(V, u, f):
    # [[V, u], [uᵀ, f]]  (eq. 1.1.2.4)
    return np.block([[V, u.reshape(2, 1)], [u.reshape(1, 2), np.array([[f]])]])

# Pencil (eq. 1.1.2.6): det is a cubic in μ → sample it, fit, find roots
mus = np.array([-3, -2, 0, 2])
dets = [np.linalg.det(augmented(V1 + m*V2, u1 + m*u2, f1 + m*f2)) for m in mus]
mu_roots = np.roots(np.polyfit(mus, dets, 3))
print("μ roots:", np.round(mu_roots.real, 4))

# Common chord: the μ where the x² terms cancel (V = 0), leaving a line
for mu in mu_roots.real:
    if np.allclose(V1 + mu*V2, 0, atol=1e-6):
        u = u1 + mu*u2; f = f1 + mu*f2
        break
print(f"Common chord: {2*u[0]:.2f}x + {2*u[1]:.2f}y + {f:.2f} = 0")

# Line as x = h + κm  (h: point on line, m: direction)
h = -f / (2 * u @ u) * u
m = np.array([-u[1], u[0]])
print("h =", h, " m =", m)

# Line–conic intersection with curve 1 (eq. 1.1.2.2)
a = m @ V1 @ m
b = m @ (V1 @ h + u1)
g = h @ V1 @ h + 2 * u1 @ h + f1
disc = b**2 - g * a
print("Discriminant:", disc)

if disc < 0:
    print("Complex κ → no real intersection. Intersections: 0")
else:
    for k in [(-b + np.sqrt(disc)) / a, (-b - np.sqrt(disc)) / a]:
        print("Point:", h + k * m)

# Plot the two curves and the common chord
x = np.linspace(-3, 2, 400)
plt.plot(x, x**2, label="y = x²")
plt.plot(x, -x**2 - 2*x - 1, "--", label="y = -x² - 2x - 1")
plt.plot(x, -x - 0.5, ":", label="common chord y = -x - 0.5")
plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(0, color="gray", linewidth=0.8)
plt.ylim(-6, 6)
plt.legend()
plt.grid(alpha=0.3)

filename = "conic_intersection.pdf"
plt.savefig(filename)
os.system(f"termux-open {filename}")

