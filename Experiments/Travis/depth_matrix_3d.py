from PIL import Image
from numpy import *
import math
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

# Open the images, make variables for plotting
left = array(Image.open('left2.png'),'f');
right = array(Image.open('right2.png'),'f');
fig = pylab.figure()
ax = Axes3D(fig)
numPoints = 0

# Calculate the values for the matrix m[rx][lx][z] and plot them
# left.shape = right.shape = [y,x,rgba]
for z in range(0, left.shape[0]):
	print "calculating plane ", z+1, " of ", left.shape[0]
	for rx in range(0, left.shape[1]):
		for lx in range(0, right.shape[1]):
			if(lx >= rx and random.random() < .000001):
				m = math.sqrt((right[z][rx][0]-left[z][lx][0])**2 + (right[z][rx][1]-left[z][lx][1])**2 + (right[z][rx][2]-left[z][lx][2])**2)
				if(m < random.random()*math.sqrt(3)):
					numPoints = numPoints + 1
					ax.scatter([rx],[lx],[z])
pyplot.show()
