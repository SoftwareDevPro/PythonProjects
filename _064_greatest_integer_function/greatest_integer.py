
import numpy
import matplotlib.pyplot as plot

def greatest_integer(x):
  return numpy.floor(x)

x = numpy.linspace(-10, 10, 10000)
y = greatest_integer(x)

fig, ax = plot.subplots()
ax.plot(x, y)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Greatest Integer Graph')

plot.show()



