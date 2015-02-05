from PIL import Image
from numpy import *
import math

# Open the images
left = array(Image.open('left.png'),'f');
right = array(Image.open('right.png'),'f');

# Retrieve the a row from each image (the same one)
row = 256
leftRow = empty([1, left.shape[1], left.shape[2]])
for i in range (0, left.shape[1]):
	for j in range (0, left.shape[2]):
		leftRow[0][i][j] = left[row][i][j]
rightRow = empty([1, right.shape[1], right.shape[2]])
for i in range (0, right.shape[1]):
	for j in range (0, right.shape[2]):
		rightRow[0][i][j] = right[row][i][j]

# Calculate the values of the disparity matrix
m = zeros([leftRow.shape[1], rightRow.shape[1]])
for i in range(0,leftRow.shape[1]):
	for j in range(0, rightRow.shape[1]):
		m[i][j] = math.sqrt((leftRow[0][i][0]-rightRow[0][j][0])**2+(leftRow[0][i][1]-rightRow[0][j][1])**2+(leftRow[0][i][2]-rightRow[0][j][2])**2)

out = Image.fromarray(uint8(m))
out.save('matrix.png')
