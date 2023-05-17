
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--level',help='the number of levels')
args = parser.parse_args()

# Generate some data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

# Create the contour plot, and show it
plt.contour(X, Y, Z, levels=int(args.level), cmap='RdYlBu')
plt.colorbar()
plt.show()
