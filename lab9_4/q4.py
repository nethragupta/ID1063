import numpy as np

# returns first i where |a[i+1]-a[i]| <= tol, else -1
def firstStable(a, n, tol):
    for i in range(n-1):
        if abs(a[i+1]-a[i]) <= tol + 0.000000001:   # difference small enough
            return i
    return -1   # never got within tolerance

a = np.array(input("Enter the readings: ").split(), dtype=float)
n = len(a)
tol = float(input("Enter tolerance: "))
print(firstStable(a, n, tol))
