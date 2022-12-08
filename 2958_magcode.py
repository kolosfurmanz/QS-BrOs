import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('data.csv', delimiter = ',', usecols = (10,11))
extinction = pd.read_csv('data.csv', delimiter = ',', usecols = (10,12))
data = data.sort_values(by = '2958 z')
extinction = extinction.sort_values(by = '2958 z')
data = data[:].values
extinction = extinction[:].values
z = []
r = []
A_v = []

for i in data:
    z.append(i[0])
    r.append(i[1])
for j in extinction: 
    A_v.append(j[1])
z = np.array(z)
r = np.array(r)
A_v = np.array(A_v)
H_0 = (69.8 + 74) / 2
c = 299792.458
def M(z, r, A_v):
    d = ((z*c*(z + 2)) / ((z + 1)**2 + 1)) / H_0
    return r - 5*np.log10(d*10**5) - A_v
plt.scatter(z, M(z, r, A_v))
plt.xlabel("Redshift (z)")
plt.ylabel("Absolute Magnitude")
plt.title("Absolute Magnitude v.s. Redshift for Plate 2958 (nQSOs = 264)")
plt.savefig("2958_mag_graph.png")
mean_mag = np.sum(M(z, r, A_v))/len(M(z, r, A_v))
print("the average absolute magnitude is", mean_mag)