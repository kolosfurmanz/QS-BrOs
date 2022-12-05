from matplotlib import pyplot as plt, colors
import numpy as np
import pandas as pd
data = np.loadtxt('1015-color-data.csv', dtype = 'float', delimiter = ',', skiprows = 1)
scale = np.loadtxt('1015-zr-data.csv', dtype = 'float', delimiter = ',', skiprows = 1)
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
x = r_i
y = i_z
c = z
df = pd.DataFrame({"x": x, "y": y, "c": c})
fig, ax = plt.subplots()
cmap = plt.cm.hot
norm = colors.Normalize(vmin = np.min(z), vmax = np.max(z))
ax.scatter(df.x, df.y, color=cmap(norm(df.c.values)))
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
cbar = fig.colorbar(sm)
cbar.set_label("Redshift (z)")
plt.xlabel('r-i')
plt.ylabel('i-z')
plt.title('r-i v.s. i-z Color Filters for Plate 1015 (nQSOs = 21)')
plt.savefig('1015_color-color_graph.png')