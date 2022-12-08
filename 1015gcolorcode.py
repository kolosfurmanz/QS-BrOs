from matplotlib import pyplot as plt, colors
import numpy as np
import pandas as pd
green_red = pd.read_csv('data.csv', delimiter = ',', usecols = (1, 15), skiprows = np.arange(22, 264))
ri_and_scale = pd.read_csv('data.csv', delimiter = ',', usecols = (0, 3), skiprows = np.arange(22, 264))
green_red = green_red.fillna(value = 0)
ri_and_scale = ri_and_scale.fillna(value = 0)
green_red = green_red[:].values
ri_and_scale = ri_and_scale[:].values
r_i = []
r = []
g = []
z = []
for i in green_red:
    r.append(i[0])
    g.append(i[1])
for j in ri_and_scale:
    z.append(j[0])
    r_i.append(j[1])
z.pop(-1)
r_i.pop(-1)
g.pop(-1)
r.pop(-1)
g_r = np.array(g) - np.array(r)
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = g_r
y = r_i
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
plt.xlabel('g-r')
plt.ylabel('r-i')
plt.xticks(np.arange(int(np.min(x)) - 1, int(np.max(x)) + 1, 1))
plt.title('r-i v.s. g-r Color Filters for Plate 1015 (nQSOs = 21)')
plt.savefig('1015_gcolor-color_graph.png')
