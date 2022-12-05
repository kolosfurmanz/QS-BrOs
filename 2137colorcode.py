from matplotlib import pyplot as plt, colors
import numpy as np
import pandas as pd
data = pd.read_csv('data.csv', delimiter = ',', usecols = (8, 9), skiprows = np.arange(52, 264))
scale = pd.read_csv('data.csv', delimiter = ',', usecols = (5, 6), skiprows = np.arange(52, 264))
data = data.fillna(value = 0)
scale = scale.fillna(value = 0)
data = data[:].values
scale = scale[:].values
r_i = []
i_z = []
z = []
for i in data:
    r_i.append(i[0])
    i_z.append(i[1])
for j in scale:
    z.append(j[0])
z.pop(-1)
r_i.pop(-1)
i_z.pop(-1)
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = r_i
y = i_z
c = z
df = pd.DataFrame({"x": x, "y": y, "c": c})
fig, ax = plt.subplots()
cmap = plt.cm.RdBu
norm = colors.Normalize(vmin = np.min(z), vmax = np.max(z))
ax.scatter(df.x, df.y, color=cmap(norm(df.c.values)))
ax.set_facecolor('grey')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
cbar = fig.colorbar(sm)
cbar.set_label("Redshift (z)")
plt.xlabel('r-i')
plt.ylabel('i-z')
plt.title('i-z v.s. r-i Color Filters for Plate 2137 (nQSOs = 51)')
plt.savefig('2137_color-color_graph.png')