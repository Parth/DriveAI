from PIL import Image
from numpy import *

# Open the images
left = array(Image.open('left.png'),'f');
right = array(Image.open('right.png'),'f');

# Retrieve the a row from each image (the same one)
row = 256
leftRow = empty([1, left.shape[1], left.shape[2]])
for i in range (0, left.shape[1]):
	for j in range (0, left.shape[2]):
		leftRow[0][i][j] = left[row][i][j]

out = Image.fromarray(uint8(leftRow))
out.save('leftrow.png')
