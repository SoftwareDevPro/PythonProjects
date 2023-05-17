
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-g','--gridsize',help='the size of the grid')
args = parser.parse_args()

# Generate some data
x = np.random.normal(size=10000)
y = np.random.normal(size=10000)

# Create the hexabin plot, show the colorbar, and show the plot
plt.hexbin(x, y, gridsize=int(args.gridsize), cmap='Greens')
plt.colorbar()
plt.show()
