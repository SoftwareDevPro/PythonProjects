
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plot

fig = plot.figure()

# set a 3d projection
ax = plot.axes(projection='3d')

# define the 3 axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)

# plotting
ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot')
plot.show()
