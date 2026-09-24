import numpy as np

# matrix from q11
P=np.array([[1,0,1],[0,1,0],[1,0,1]])

# eigenvalues, rounded and sorted
ev=np.sort(np.round(np.linalg.eigvals(P).real,4))
print("eigenvalues :",ev)

# A - trace should equal sum of eigenvalues
tr=np.trace(P)
print("A : trace =",tr,", sum of eigenvalues =",ev.sum(),"-> TRUE")

# B - if PᵀP = I then det has to be +1 or -1
print("B : det(P) =",round(np.linalg.det(P),4),", needs to be +-1 -> FALSE")

# C - skew symmetric means Pᵀ = -P
print("C : Pᵀ = P so its symmetric, not skew -> FALSE")

# D - check magnitude of each eigenvalue
print("D : |eigenvalues| =",np.abs(ev),", not all 1 -> FALSE")

print("ans : A")    

