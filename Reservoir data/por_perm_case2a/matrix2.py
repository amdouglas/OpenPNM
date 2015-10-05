import numpy as np

z = 220 #Dimensions
x = 85
y = 60
a = np.arange(y) #1-D array

data = np.loadtxt("spe_phi_sample.prn")

print(data)

result = np.tile(data[None, :, None], (x, y, z))
print (result.shape)


#y,z,x = result.nonzero()

#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(x, y, -z, zdir='z', c= 'red')