import numpy as np

#Get the Data

#Permeability data

data_perm = np.fromfile('spe_perm.dat', sep=' ')
rockperm = np.reshape(data_perm, -1, 3)
print(rockperm.shape)

#Porosity Data

data_poro = np.fromfile('spe_phi.dat', sep=' ')
rockporo = np.reshape(data_poro, -1, 1)
print(rockporo.shape)


#Create the array
[Nx, Ny, Nz] = (60, 220, 85)
[I, J, K]    = (np.arange(1,Nx+1,1),np.arange(1,Ny+1,1),np.arange(1,Nz+1,1))

[I, J, K] = np.meshgrid(I, J, K)

print([I])

ix=np.ravel_multi_index((Nx,Ny,Nz), (I[:], J[:], K[:]), order='F')

print(ix)


#print(data.shape)

#data = np.reshape(data, (220,85,1))

#print(data.shape)

#x,y,z = data.nonzero()

#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')


#ax.scatter(x, y, -z, c=data[x,y,z] ,  zdir='z')

#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')