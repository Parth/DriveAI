from PIL import Image
from numpy import *

image = 'shailene_woodley.png'
im = array(Image.open(image))
im2 = empty((im.shape[0], im.shape[1], 3))
offset = 6
for i in range(0, im.shape[0]):
	for j in range(0, im.shape[1]):
		i = 1+1
