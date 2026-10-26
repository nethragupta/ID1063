"""
GATE 2025 CS1 Q58: PDF p(x) = C x^2 on [1, 4], find P(2 <= X <= 3).
1. Derive the CDF F(x) numerically and analytically, plot it.
2. Use F to get P(2 <= X <= 3) = F(3) - F(2).
3. Use the inverse CDF to generate the random variable X (inverse transform
   sampling) and check the probability by simulation.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")              # no screen needed (works in Termux)
import matplotlib.pyplot as plt

a, b = 1, 4


def quad(f, lo, hi, n=200001):
    """Numerical integral with the trapezoid rule (no scipy needed)."""
    x = np.linspace(lo, hi, n)
    return np.trapezoid(f(x), x) if hasattr(np, "trapezoid") else np.trapz(f(x), x), 0


# --- Normalising constant: C * integral(x^2, 1, 4) = 1 ---
area, _ = quad(lambda x: x**2, a, b)
C = 1 / area                       # = 1/21


def pdf(x):
    x = np.asarray(x, dtype=float)
    return np.where((x >= a) & (x <= b), C * x**2, 0.0)


def cdf(x):
    """F(x) = 0 (x<1), (x^3 - 1)/63 (1<=x<=4), 1 (x>4)"""
    x = np.asarray(x, dtype=float)
    return np.clip((x**3 - a**3) * C / 3, 0, 1)


def cdf_inverse(u):
    """Solve u = (x^3 - 1)/63  ->  x = (63u + 1)^(1/3)"""
    return (3 * u / C + a**3) ** (1 / 3)


# --- Probability from the CDF ---
p_theory = cdf(3) - cdf(2)
p_numeric, _ = quad(pdf, 2, 3)
print(f"C                    = {C:.6f}  (1/21 = {1/21:.6f})")
print(f"F(3) - F(2)          = {p_theory:.6f}  (19/63 = {19/63:.6f})")
print(f"Direct integral 2..3 = {p_numeric:.6f}")

# --- Generate X from the CDF (inverse transform sampling) ---
rng = np.random.default_rng(0)
N = 1_000_000
U = rng.uniform(0, 1, N)
X = cdf_inverse(U)
p_sim = np.mean((X >= 2) & (X <= 3))
print(f"Simulated P(2<=X<=3) = {p_sim:.6f}  ({N:,} samples)")

# --- Plots ---
xs = np.linspace(0, 5, 1000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

ax1.plot(xs, cdf(xs), lw=2, label="Theoretical CDF $F(x)=(x^3-1)/63$")
xe = np.sort(X[:5000])
ax1.step(xe, np.arange(1, len(xe) + 1) / len(xe), where="post",
         ls="--", lw=1.2, label="Empirical CDF (simulated X)")
for xv in (2, 3):
    ax1.plot([xv, xv], [0, cdf(xv)], "k:", lw=1)
    ax1.plot(xv, cdf(xv), "ro")
ax1.annotate(f"F(3)-F(2) = {p_theory:.3f}", xy=(3, cdf(3)),
             xytext=(3.3, 0.25), arrowprops=dict(arrowstyle="->"))
ax1.set(xlabel="x", ylabel="F(x)", title="CDF of X")
ax1.grid(alpha=0.3)
ax1.legend(loc="upper left")

ax2.hist(X, bins=150, density=True, alpha=0.5, label="Histogram of simulated X")
ax2.plot(xs, pdf(xs), "r", lw=2, label="PDF $x^2/21$")
mask = (xs >= 2) & (xs <= 3)
ax2.fill_between(xs[mask], pdf(xs[mask]), alpha=0.3, color="green",
                 label=f"P(2≤X≤3) ≈ {p_theory:.3f}")
ax2.set(xlabel="x", ylabel="p(x)", title="PDF vs generated samples")
ax2.grid(alpha=0.3)
ax2.legend(loc="upper left")

plt.tight_layout()
plt.savefig("cdf_q58.pdf")
print("Saved plot to cdf_q58.pdf")

# Open the PDF in the phone's default viewer (needs: pkg install termux-tools)
import os
os.system("termux-open cdf_q58.pdf")

