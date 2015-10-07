
#a=np.empty((2,3,5))


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Import data

data = np.loadtxt("spe_phi.dat")

i = 2
j = 3
k = 4
a = np.arange(k)

t = np.tile(a,j*i).reshape((i,j,k))


print(t)

for x in np.nditer(data):
    print (x)


#PLot stuff
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(X,Y,X, c = 'r', marker = 'o')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()
