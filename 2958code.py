import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('data.csv', delimiter = ',', usecols = (10, 14))
sort = data.sort_values(by = '2958 z')
sort = sort.fillna(value = 0)
sort = sort[:].values
z = []
r = []

for i in sort:
    z.append(i[0])
    r.append(i[1])
z.pop(-1)
r.pop(-1)
z = np.array(z)
r = np.array(r)

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
plt.title("i-z Color Filter v.s. Redshift for Plate 2958 (nQSOs = 264)")
plt.xlabel("Redshift (z)")
plt.ylabel("i-z Color Filter")
plt.savefig('2958_izz_graph.png')
print("the r^2 score is", R2)
mean_z = np.sum(z)/len(z)
print("the average redshift value is", mean_z)
print("the slope is", m)
print("the i-z intercept is", b)
print(z)