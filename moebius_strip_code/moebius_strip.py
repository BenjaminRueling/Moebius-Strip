import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = np.linspace(0, 2* np.pi, 100)
v = np.linspace(-1,1,100)
u, v = np.meshgrid(u, v)
x = (1 + 0.5 * v * np.cos(u/2)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u/2)) * np.sin(u)
z = 0.5 * v * np.sin(u/2)

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.plot_surface(x,y,z, cmap = "viridis")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Möbius Strip")

plt.show()
plt.savefig("Möbius Strip")