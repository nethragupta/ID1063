import numpy as np

P=np.array([[1,0,1],[0,1,0],[1,0,1]])

ev = np.linalg.eigvals(P)
ev=np.round(ev.real,4)
print("eigenvalues:",sorted(ev))

# A
tr=np.trace(P)
print("A :",tr,"vs",sum(ev),"->",np.isclose(tr,sum(ev)))

# B
pp = P.T@P
print("B :",np.array_equal(pp,np.eye(3)))
print(pp)

# C
print("C :",np.array_equal(P.T,-P))

# D
print("D :",np.allclose(abs(ev),1))

