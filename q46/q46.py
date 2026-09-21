import os
import numpy as np
import matplotlib.pyplot as plt

# f(x) = sin(2x) for x > 0, a + b*x for x <= 0
# differentiable at 0 means the function value and the slope match from both sides

h = 1e-6

# right side gives the values we need to match
a = np.sin(2 * h)                    # continuity: a = f(0+)
b = (np.sin(2 * h) - 0) / h          # slope: b = f'(0+)
a = round(a, 4)
b = round(b, 4)
print("a =", a)
print("b =", b)
print("a + b =", a + b)


def f(x):
    return np.where(x > 0, np.sin(2 * x), a + b * x)


# check both conditions using the values we found
left_val = f(-h)
right_val = f(h)
left_slope = (f(0) - f(-h)) / h
right_slope = (f(h) - f(0)) / h

print("\nvalue  left, right:", float(left_val), float(right_val))
print("slope  left, right:", float(left_slope), float(right_slope))

if abs(left_val - right_val) < 1e-4 and abs(left_slope - right_slope) < 1e-4:
    print("differentiable at x = 0")
else:
    print("NOT differentiable at x = 0")

# try a wrong b to see the difference
b_wrong = 1
slope_wrong = (0 - (a + b_wrong * (-h))) / h
print("\nwith b = 1 the left slope is", round(slope_wrong, 3), "but the right slope is", round(float(right_slope), 3))

x = np.linspace(-3, 3, 1000)
plt.plot(x, f(x), label="f(x)")
plt.plot(x, b * x + a, "--", color="gray", label="tangent y = 2x")
plt.plot(0, 0, "ro")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.ylim(-4, 4)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("a = %g, b = %g, a + b = %g" % (a, b, a + b))
plt.legend()
plt.grid(True)

fname = "q46.pdf"
plt.savefig(fname)

os.system('termux-open q46.pdf')

