from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random

fig = pylab.figure()
ax = Axes3D(fig)

ax.scatter([0],[1],[2])
ax.scatter([3],[2],[1])
pyplot.show()
