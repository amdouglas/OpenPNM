import numpy as np

z = 220/5 #Dimensions
x = 85/5
y = 60/5
a = np.arange(y) #1-D array

import numpy as np

a = np.loadtxt("spe_phi.dat")

result = np.tile(a[None, :, None], (x, 1, z))
print (result.shape)

#Re-shape
#t = np.tile(a,z*x).reshape((x,z,y))
#print(t.shape)

y,z,x = result.nonzero()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, -z, zdir='z', c= 'red')