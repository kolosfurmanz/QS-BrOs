from matplotlib import pyplot as plt, colors
import numpy as np
import pandas as pd
data = pd.read_csv('data.csv', delimiter = ',', usecols = (13, 14))
scale = pd.read_csv('data.csv', delimiter = ',', usecols = (10, 11))
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
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
np.flip(r_i, 0)
np.flip(i_z, 0)
np.flip(z, 0)
x = r_i
y = i_z
c = z
df = pd.DataFrame({"x": x, "y": y, "c": c})
fig, ax = plt.subplots()
cmap = plt.cm.RdBu_r
norm = colors.Normalize(vmin = np.min(z), vmax = np.max(z))
ax.scatter(df.x, df.y, color=cmap(norm(df.c.values)))
ax.set_facecolor('grey')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
cbar = fig.colorbar(sm)
cbar.set_label("Redshift (z)")
plt.xlabel('r-i')
plt.ylabel('i-z')
plt.title('i-z v.s. r-i Color Filters for Plate 2958 (nQSOs = 264)')
plt.savefig('2958_color-color_graph.png')