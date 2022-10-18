

import matplotlib.pyplot as plot    

# define the labels, and associated data
labels = [ "Ruby", "Python", "Java", "HTML", "C++", "Javascript" ]
data = [ 85, 75, 85, 60, 85, 95 ]

# define the pie sections that cutout from the pie
cutout  = [ 0.0, 0.0, 0.0, 0.1, 0.0, 0.2 ]

# set the piechart, and show it
plot.pie(data, labels=labels, explode=cutout)
plot.show()

