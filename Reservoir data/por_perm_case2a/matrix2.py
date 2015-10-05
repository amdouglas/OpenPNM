import numpy as np

data = np.loadtxt("spe_phi_sample.prn")

print(data.shape)

data = data.reshape(85,60,2)

print(data.shape)

x,y,z = data.nonzero()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(-z, x, y, c=y ,  zdir='z')

ax.set_xlabel('Z')
ax.set_ylabel('X')
ax.set_zlabel('Y')