import numpy as np

a = np.arange(24).reshape((4,6))

# If I select certain rows, it works
print(a.size)

a[1:7:2]

print(a[[0, 1, 3], :])

for x in np.nditer(a):
    print (x)


# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [12, 13, 14, 15]])

# If I select certain rows and a single column, it works
print(a[[0, 1, 2, 3], 2])
# array([ 2,  6, 14])