from PIL import Image
from numpy import *
import math
from multiprocessing import Process

row = 256
lR = None
rR = None

def toautomate1():
	# Open the images
	left = array(Image.open('left2.png'),'f');
	leftRow = empty([1, left.shape[1], left.shape[2]])
	for i in range (0, left.shape[1]):
		for j in range (0, left.shape[2]):
			leftRow[0][i][j] = left[row][i][j]
	lR = leftRow
	print  lR, "4"
	print lR, "5"

def toautomate2():
	# Open the images
	right = array(Image.open('right2.png'),'f');
	rightRow = empty([1, right.shape[1], right.shape[2]])
	for i in range (0, right.shape[1]):
		for j in range (0, right.shape[2]):
			rightRow[0][i][j] = right[row][i][j]
	rR = rightRow

def save(leftRow, rightRow):
	# Calculate the values of the disparity matrix
	m = zeros([leftRow.shape[1], rightRow.shape[1]])
	for i in range(0,leftRow.shape[1]):
		for j in range(0, rightRow.shape[1]):
			m[i][j] = math.sqrt((leftRow[0][i][0]-rightRow[0][j][0])**2+(leftRow[0][i][1]-rightRow[0][j][1])**2+(leftRow[0][i][2]-rightRow[0][j][2])**2)

	out = Image.fromarray(uint8(m))
	out.save('matrix2.png')

if __name__ == '__main__':
	print lR, "1"
	a = Process(target=toautomate1)
	b = Process(target=toautomate2)

	a.start()
	b.start()
	a.join()
	b.join()
	print lR, "2"
