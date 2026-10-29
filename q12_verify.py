"""GATE 2026 EC Q12: unit normal to z^2 = 2x^2 - y^2 at P = (1, 0, sqrt2).

Verifies the matrix method (n along M @ P) and plots the surface with the normal.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Surface as a quadratic form: f(x) = x^T M x = 2x^2 - y^2 - z^2 = 0
M = np.diag([2.0, -1.0, -1.0])
P = np.array([1.0, 0.0, np.sqrt(2)])

def f(v):
    return v @ M @ v

print("1) P on the surface?   f(P) =", round(f(P), 12))

# Matrix method: normal is along M @ P
v = M @ P
n = v / np.linalg.norm(v)
print("2) M @ P               =", v)
print("   unit normal n       =", n)

# Option (D): (sqrt2 i - k)/sqrt3
D = np.array([np.sqrt(2), 0.0, -1.0]) / np.sqrt(3)
print("   option (D)          =", D)
print("   n matches (D)?      ", np.allclose(n, D))

# Independent check: numerical gradient by central differences
h = 1e-6
grad = np.array([(f(P + h * e) - f(P - h * e)) / (2 * h) for e in np.eye(3)])
print("3) numerical grad f(P) =", grad.round(6), " (should equal 2*M@P =", 2 * v, ")")

# Tangent vectors from the parametrisation x = r/sqrt2, y = r cos t, z = r sin t
# (P is at r = sqrt2, t = pi/2)
r, t = np.sqrt(2), np.pi / 2
T_r = np.array([1 / np.sqrt(2), np.cos(t), np.sin(t)])
T_t = np.array([0.0, -r * np.sin(t), r * np.cos(t)])
print("4) n . T_r             =", round(n @ T_r, 12))
print("   n . T_t             =", round(n @ T_t, 12))
print("   |n|                 =", round(np.linalg.norm(n), 12))

# Other options: unit length and parallel to n?
opts = {
    "A": np.array([1.0, 0.0, -np.sqrt(2)]),
    "B": np.array([2 / 3, 0.0, -1 / 3]),
    "C": np.array([np.sqrt(2), 0.0, -np.sqrt(3)]),
    "D": D,
}
print("5) option  |vec|    parallel to n?")
for k, o in opts.items():
    par = np.allclose(np.cross(o, n), 0)
    print(f"   ({k})    {np.linalg.norm(o):.4f}   {par}")

# ---------- Plot ----------
# 2x^2 = y^2 + z^2 is a double cone around the x-axis
rr = np.linspace(-2.2, 2.2, 60)
tt = np.linspace(0, 2 * np.pi, 80)
R, Tt = np.meshgrid(rr, tt)
X = R / np.sqrt(2)
Y = R * np.cos(Tt)
Z = R * np.sin(Tt)

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, Z, alpha=0.35, color="tab:blue", edgecolor="none")

# Tangent plane patch at P
a, b = np.meshgrid(np.linspace(-0.6, 0.6, 2), np.linspace(-0.6, 0.6, 2))
u1 = T_r / np.linalg.norm(T_r)
u2 = T_t / np.linalg.norm(T_t)
plane = P[:, None, None] + u1[:, None, None] * a + u2[:, None, None] * b
ax.plot_surface(*plane, alpha=0.5, color="tab:green")

ax.scatter(*P, color="k", s=40)
ax.text(*(P + 0.1), "P (1, 0, √2)")
ax.quiver(*P, *n, length=1.0, color="red", linewidth=2.5, arrow_length_ratio=0.15)
ax.quiver(*P, *(-n), length=1.0, color="orange", linewidth=2.5, arrow_length_ratio=0.15)
ax.text(*(P + 1.05 * n), "n = (√2 î − k̂)/√3", color="red")
ax.text(*(P - 1.1 * n), "−n", color="orange")

ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_title("z² = 2x² − y²  with unit normal at P (green = tangent plane)")
ax.set_box_aspect([1, 1, 1])
ax.view_init(elev=18, azim=-60)
plt.tight_layout()
out = "q12_normal.pdf"
plt.savefig(out)
print("Saved plot to", out)

# Open the PDF automatically (Termux on Android, Linux, macOS, Windows)
import os, shutil, subprocess, sys
if shutil.which("termux-open"):
    subprocess.run(["termux-open", out])
elif sys.platform.startswith("win"):
    os.startfile(out)
elif sys.platform == "darwin":
    subprocess.run(["open", out])
elif shutil.which("xdg-open"):
    subprocess.run(["xdg-open", out])

# Open the PDF automatically (termux-open on Android/Termux, else desktop openers)
import shutil, subprocess, sys
for opener in ("termux-open", "xdg-open", "open"):
    if shutil.which(opener):
        subprocess.run([opener, "q12_normal.pdf"])
        break
else:
    print("No PDF opener found; open q12_normal.pdf manually.", file=sys.stderr)

