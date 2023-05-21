

import numpy
import matplotlib.pyplot as plot

x = numpy.linspace(-20, 20, 500)
y1 = -numpy.sqrt(x ** 2 - 1)
y2 = numpy.sqrt(x ** 2 - 1)

fig, ax = plot.subplots()
ax.plot(x, y1, color='blue', label='y = -sqrt(x^2 - 1)')
ax.plot(x, y2, color='red', label='y = +sqrt(x^2 - 1)')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Hyperbola')

plot.show()


