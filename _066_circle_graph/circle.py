
import numpy
import matplotlib.pyplot as plot

r = 10
x0 = 1
y0 = 1

t = numpy.linspace(0, 2*numpy.pi, 1000)
x = x0 + r * numpy.cos(t)
y = y0 + r * numpy.sin(t)

fig, ax = plot.subplots()
ax.plot(x, y)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Circle Graph')

plot.show()

