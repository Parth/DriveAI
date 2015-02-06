from PIL import Image
from numpy import *
import math
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
from multiprocessing import Pool

# Open the images, make variables for plotting
left = array(Image.open('left2.png'),'f');
right = array(Image.open('right2.png'),'f');
PROCESSES = 8

def compute(z):
	for rx in range(0, left.shape[1]):
		for lx in range(0, right.shape[1]):
			m = math.sqrt((right[z][rx][0]-left[z][lx][0])**2 + (right[z][rx][1]-left[z][lx][1])**2 + (right[z][rx][2]-left[z][lx][2])**2)
	return m

if __name__ == '__main__':
	p = Pool(PROCESSES)
	m = p.map(compute, range(0, 8))
	print m
