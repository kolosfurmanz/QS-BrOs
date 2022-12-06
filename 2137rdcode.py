import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
data = pd.read_csv('data.csv', delimiter = ',', usecols = (5,6), skiprows = np.arange(52, 264))
data = data.fillna(value = 0)
data = data[:].values
z = []
for i in data:
    z.append(i[0])
z.pop(-1)
z = np.sort(z)
H_0 = (69.8 + 74) / 2
c = 299792.458
def d(z):
    return ((z*c*(z + 2)) / ((z + 1)**2 + 1)) / H_0
def highd(z):
    return ((z*c*(z + 2)) / ((z + 1)**2 + 1)) / 69.8
def lowd(z):
    return ((z*c*(z + 2)) / ((z + 1)**2 + 1)) / 74
error = highd(z) - lowd(z)
plt.scatter(z, d(z))
plt.errorbar(z, d(z), yerr = error, fmt = "o")
plt.xlabel("Redshift (z)")
plt.ylabel("Distance (Mpc)")
plt.title("Distance v.s. Redshift for Plate 2137 (nQSOs = 51)")
plt.savefig('2137_rd_graph.png')
mean_d = np.sum(d(z)) / len(d(z))
print("the average distance is", mean_d, "Mpc")