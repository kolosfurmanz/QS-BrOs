import numpy as np 
import matplotlib.pyplot as plt
data = np.loadtxt('2958-zr-data.csv', dtype = 'float', delimiter = ',', skiprows = 1)
z = []
r = []

for i in data:
    z.append(i[0])
    r.append(i[1])
z = np.sort(z)
r = np.sort(r)


n = np.size(z)
mean_z = np.mean(z)
mean_r = np.mean(r)
SS_zr = np.sum(r*z) - n*mean_r*mean_z
SS_zz = np.sum(z*z) - n*mean_z*mean_z
m = SS_zr / SS_zz 
b = mean_r - m*mean_z
line = m*z + b 
error = r - line
square_error = np.sum(error**2)
meanse = square_error / n
root_meanse = np.sqrt(meanse)
SSt = np.sum((r - mean_r)**2)
R2 = 1 - (square_error / SSt)
plt.scatter(z, r)
plt.plot(z, line)
plt.title("Redshift v.s. Red Color Filter for Plate 2958 (nQSO = 264)")
plt.xlabel("Redshift (z)")
plt.ylabel("Red color filter (r)")
plt.savefig('2958_zr_graph.png')
print("the r^2 score is:", R2)
mean_z = np.sum(z)/len(z)
print("the average redshift value is", mean_z)