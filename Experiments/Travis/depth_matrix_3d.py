from PIL import Image
from numpy import *
import math
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

# Open the images
left = array(Image.open('left2.png'),'f');
right = array(Image.open('right2.png'),'f');

# Calculate the values for the matrix m[rx][lx][z]
# left.shape = right.shape = [y,x,rgba]
print "allocating array..."
m = zeros([left.shape[1], right.shape[1], left.shape[0]])
for z in range(0, left.shape[0]):
	print "calculating plane ", z+1, " of ", left.shape[0]
	for rx in range(0, left.shape[1]):
		if (rx % 10 == 0)
			print "\trow ", rx, " of ", left.shape[1]
		for lx in range(0, right.shape[1]):
			m[rx][lx][z] = math.sqrt((right[z][rx][0]-left[z][lx][0])**2 + (right[z][rx][1]-left[z][lx][1])**2 + (right[z][rx][2]-left[z][lx][2])**2)
