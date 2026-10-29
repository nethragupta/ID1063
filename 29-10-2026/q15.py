"""GATE 2026 EC Q15: x1 = cos(20*pi*t), x2 = cos(100*pi*t), sampled at Fs = 40 Hz.

Checks the first ten samples and plots both signals with their samples.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

Fs = 40
n = np.arange(10)          # first ten samples, starting at t = 0
ts = n / Fs

x1 = np.cos(20 * np.pi * ts)
x2 = np.cos(100 * np.pi * ts)

print(" n   x1[n]    x2[n]")
for k in n:
    print(f"{k:2d}  {x1[k]:6.3f}   {x2[k]:6.3f}")

print()
print("(A) first 3: all x1 > x2 ?", bool(np.all(x1[:3] > x2[:3])))
print("(B) last 3:  all x1 > x2 ?", bool(np.all(x1[-3:] > x2[-3:])))
print("(C) all x2 > x1 ?         ", bool(np.all(x2 > x1)))
print("(D) 4th-7th equal ?       ", bool(np.allclose(x1[3:7], x2[3:7])))
print("All ten samples equal ?   ", bool(np.allclose(x1, x2)))

# ---------- Plot ----------
t = np.linspace(0, 9.5 / Fs, 2000)
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(t, np.cos(20 * np.pi * t), label="x1(t) = cos(20πt)  (10 Hz)", lw=2)
ax.plot(t, np.cos(100 * np.pi * t), label="x2(t) = cos(100πt)  (50 Hz)", lw=1, alpha=0.7)
ax.stem(ts, x2, linefmt="k:", markerfmt="ko", basefmt=" ", label="samples (Fs = 40 Hz)")
for k in n:
    ax.annotate(f"n={k}", (ts[k], x1[k]), textcoords="offset points",
                xytext=(0, 8 if x1[k] >= 0 else -14), ha="center", fontsize=8)
ax.set_xlabel("t (s)")
ax.set_ylabel("amplitude")
ax.set_title("Q15: both signals give identical samples at Fs = 40 Hz (aliasing)")
ax.legend(loc="lower right", fontsize=8)
ax.grid(alpha=0.3)
plt.tight_layout()

out = "q15.pdf"
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

