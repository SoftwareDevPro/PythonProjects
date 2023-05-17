
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b','--bins',help='the number of bins')
args = parser.parse_args()

# Generating some random data
data = np.random.randn(10000, 50)

# Creating a 2D histogram, add a color bar, and show the plot
plt.hist2d(data[:,0], data[:,1], bins=int(args.bins))
plt.colorbar()
plt.show()

