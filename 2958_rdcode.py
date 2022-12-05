import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
data = pd.read_csv('data.csv', delimiter = ',', usecols = (10,11))
data = data[:].values
z = []
for i in data:
    z.append(i[0])
z = np.sort(z)
H_0 = (69.8 + 74) / 2
c = 299792.458
def d(z):
    return ((z*c*(z + 2)) / ((z + 1)**2 + 1)) / H_0
plt.scatter(z, d(z))
plt.xlabel("Redshift (z)")
plt.ylabel("Distance (Mpc)")
plt.title("Distance v.s. Redshift for Plate 2958 (nQSOs = 264)")
plt.savefig('2958_rd_graph.png')
