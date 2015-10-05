import numpy as np

#data = np.loadtxt("spe_phi_sample.prn")
data = np.genfromtxt("spe_phi_sample.csv", delimiter=',')

#Try importing csv, see if it is a 1-d array


print(data.shape)

data = np.reshape(data, (85,1,220))

print(data.shape)

x,y,z = data.nonzero()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, -z, c=data[x,y,z] ,  zdir='z')

#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')