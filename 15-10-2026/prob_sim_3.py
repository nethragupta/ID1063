import numpy as np

# P(x) = C x^2 on [1, 4], 0 elsewhere
C = 1 / 21                       # from integral of C x^2 over [1,4] = 1
exact = C * (3**3 - 2**3) / 3    # = 19/63

# Inverse-transform sampling: F(x) = (x^3 - 1)/63  ->  x = (63u + 1)^(1/3)
rng = np.random.default_rng(42)
N = 1_000_000
u = rng.random(N)
x = np.cbrt(63 * u + 1)

sim = np.mean((x >= 2) & (x <= 3))

print(f"C                  = {C:.6f}")
print(f"Exact P(2<=x<=3)   = {exact:.6f}  -> {exact:.3f}")
print(f"Simulated (N={N}) = {sim:.6f}  -> {sim:.3f}")
print(f"Absolute error     = {abs(sim - exact):.6f}")

# ---------------- Plot ----------------
# Termux has no display, so render off-screen and save to a file instead
import os
import shutil
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

xs = np.linspace(0, 5, 1000)
pdf = np.where((xs >= 1) & (xs <= 4), C * xs**2, 0.0)

fig, ax = plt.subplots(figsize=(8, 5))

# Histogram of simulated samples (normalised to a density)
ax.hist(x, bins=100, density=True, alpha=0.35, color="tab:blue",
        label=f"Simulated samples (N={N:,})")

# Theoretical PDF curve
ax.plot(xs, pdf, color="tab:red", lw=2, label=r"Theoretical $P(x)=x^2/21$")

# Shade the region 2 <= x <= 3
mask = (xs >= 2) & (xs <= 3)
ax.fill_between(xs[mask], pdf[mask], color="tab:orange", alpha=0.6,
                label=f"$P(2\\leq x\\leq 3)$: exact {exact:.3f}, sim {sim:.3f}")

ax.set_xlabel("x")
ax.set_ylabel("P(x)")
ax.set_title(r"PDF $P(x)=Cx^2$ on $[1,4]$, $C=1/21$")
ax.set_xlim(0, 5)
ax.grid(alpha=0.3)
ax.legend()
plt.tight_layout()

# Save to the phone's Downloads folder if Termux storage is set up,
# otherwise to the current folder
downloads = os.path.expanduser("~/storage/downloads")
out_dir = downloads if os.path.isdir(downloads) else os.getcwd()
out_path = os.path.join(out_dir, "pdf_plot.pdf")
plt.savefig(out_path, format="pdf")
plt.close(fig)
print(f"Plot saved to      : {out_path}")

# Open the PDF in the phone's default PDF viewer (needs the termux-tools package)
if shutil.which("termux-open"):
    subprocess.run(["termux-open", out_path])

