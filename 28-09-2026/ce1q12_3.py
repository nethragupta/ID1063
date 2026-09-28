#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL


import sys                                          #for path to external scripts
sys.path.insert(0, '/data/data/com.termux/files/home/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

#Given normals
n1 = np.array(([1, 1, 1])).reshape(-1,1)
n2 = np.array(([1, 0, 2])).reshape(-1,1)
N = np.block([n1,n2]).T

#Rank and nullity
r = LA.matrix_rank(N)
print('rank =', r)
print('nullity =', N.shape[1]-r)

#Direction vector of the line
m = np.cross(n1.T,n2.T).T
print('direction vector m = n1 x n2 =', m.T)
print('norm of m =', LA.norm(m))

#Points on the line
A = np.array(([0, 0, 0])).reshape(-1,1)
B = -m
C = m
print('rank of [B-A, C-A] =', LA.matrix_rank(np.block([B-A,C-A])))
print('nullity = 1, so the solution set is a line -> ans : B')

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

#Planes
a, b, c, d = 1, 1, 1, 0
Z = (-a*X - b*Y - d) / c
ax.plot_surface(X, Y, Z, alpha=0.5)

a, b, c, d = 1, 0, 2, 0
Z = (-a*X - b*Y - d) / c
ax.plot_surface(X, Y, Z, alpha=0.5,color="grey")

#Labeling the coordinates
colors = np.arange(2, 5)
tri_coords = np.block([A, B, C])
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i],f'{txt}',fontsize=12, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)
ax.set_box_aspect([1,1,1])
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('ce1q12.pdf')
subprocess.run(shlex.split("termux-open ce1q12.pdf"))
#else
#plt.show()

