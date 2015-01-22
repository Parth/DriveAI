from numpy import *
from PIL import Image
import imtools

image = 'shailene_woodley.png'
im = array(Image.open(image))
im2 = empty((im.shape[0], im.shape[1], 3))
offset = 6
for i in range(0, im.shape[0]):
	for j in range(0, im.shape[1]):
		if i+1 < im.shape[0] and i-1 >= 0 and j+1 < im.shape[1] and j-1 >= 0:
			dxr = im[i-1,j,0]*.5-im[i+1,j,0]*.5
			dxg = im[i-1,j,1]*.5-im[i+1,j,1]*.5
			dxb = im[i-1,j,2]*.5-im[i+1,j,2]*.5
			xGrad = sqrt((dxr**2+dxg**2+dxb**2)*2/3)
			im2[i,j,0] = xGrad
			
			dyr = im[i,j-1,0]*.5-im[i,j+1,0]*.5
			dyg = im[i,j-1,1]*.5-im[i,j+1,1]*.5
			dyb = im[i,j-1,2]*.5-im[i,j+1,2]*.5
			yGrad = sqrt((dyr**2+dyg**2+dyb**2)*2/3)
			im2[i,j,1] = yGrad
			
			im2[i,j,2] = sqrt(xGrad**2+yGrad**2) 
	if i%40 == 0:
		print "calculating row: ", i
rMin = 255
gMin = 255
bMin = 255
rMax = 0
gMax = 0
bMax = 0
for i in range(0, im.shape[0]):
	for j in range(0, im.shape[1]):
		if i+1 < im.shape[0] and i-1 >= 0 and j+1 < im.shape[1] and j-1 >= 0:
			rMin = min(rMin, im2[i,j,0])
			gMin = min(gMin, im2[i,j,1])
			bMin = min(bMin, im2[i,j,2])
			rMax = max(rMax, im2[i,j,0])
			gMax = max(gMax, im2[i,j,1])
			bMax = max(bMax, im2[i,j,2])
	if i%40 == 0:
		print "analyzing row: ", i
print "rMin = ", rMin
print "gMin = ", rMin
print "bMin = ", rMin
print "rMax = ", rMax
print "gMax = ", rMax
print "bMax = ", rMax
for i in range(0, im.shape[0]):
	for j in range(0, im.shape[1]):
		if i+1 < im.shape[0] and i-1 >= 0 and j+1 < im.shape[1] and j-1 >= 0:
			im2[i,j,0] = (im2[i,j,0]-rMin)*256/rMax
			im2[i,j,1] = (im2[i,j,1]-gMin)*256/gMax
			im2[i,j,2] = (im2[i,j,2]-bMin)*256/bMax
	if i%40 == 0:
		print "normalizing row: ", i
print "...done"
out = Image.fromarray(uint8(im2))
out.save('output.png')
