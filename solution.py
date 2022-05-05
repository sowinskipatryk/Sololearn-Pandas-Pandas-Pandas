"""
input format example:
3 <- number of data points
1 1 <- two numeric values separated with space (one data point)
0 1
2 1
"""

import numpy as np

# Number of data points
n = int(input())

# Given initial centroids
c1 = np.array([0., 0.])
c2 = np.array([2., 2.])

# Cluster lists
cluster1 = []
cluster2 = []

# Collecting inputs, calculating the euclidean distance between the centroid
# and each point determining the cluster it is assigned to
for _ in range(n):
    x, y = input().split()
    p = np.array([float(x), float(y)])
    dist1 = np.sqrt((p[0]-c1[0])**2 + (p[1]-c1[1])**2)
    dist2 = np.sqrt((p[0]-c2[0])**2 + (p[1]-c2[1])**2)
    if dist1 <= dist2:
        cluster1.append(p)
    else:
        cluster2.append(p)

# Converting lists to arrays
cluster1 = np.array(cluster1)
cluster2 = np.array(cluster2)

# Checking cluster size, assigning None if it's empty, otherwise counting
# the new centroids as the mean value of each point's x and y value and rounding
# them up to second decimal place
if cluster1.size:
    new_c1 = np.round([np.mean(cluster1[:,i]) for i in range(2)], decimals=2)
else:
    new_c1 = None
if cluster2.size:
    new_c2 = np.round([np.mean(cluster2[:,i]) for i in range(2)], decimals=2)
else:
    new_c2 = None

# Printing the results - new centroids
print(new_c1)
print(new_c2)
