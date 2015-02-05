from PIL import Image
from numpy import *
from scipy.ndimage import filters

# Open the images. They are assumed to be of the same dimensions.
left = array(Image.open('left.png'),'f')
right = array(Image.open('right.png'),'f')

# Make highly multichannel 'metaimage' with c channels. These will store metainformation.
c = 9
l = empty([left.shape[0],left.shape[1],c])
r = empty([right.shape[0],right.shape[1],c])
for i in range(0,3):
	l[:,:,i] = left[:,:,i]
	r[:,:,i] = right[:,:,i]

# Calculate x and y derivates of each color channel for each image. Add to metaimage.
lx = empty(left.shape)
ly = empty(left.shape)
rx = empty(right.shape)
ry = empty(right.shape)
print "sobel filter 1  (of 12)"
filters.sobel(left[:,:,0],1,lx[:,:,0])
print "sobel filter 2  (of 12)"
filters.sobel(left[:,:,1],1,lx[:,:,1])
print "sobel filter 3  (of 12)"
filters.sobel(left[:,:,2],1,lx[:,:,2])
print "sobel filter 4  (of 12)"
filters.sobel(left[:,:,0],0,ly[:,:,0])
print "sobel filter 5  (of 12)"
filters.sobel(left[:,:,1],0,ly[:,:,1])
print "sobel filter 6  (of 12)"
filters.sobel(left[:,:,2],0,ly[:,:,2])
print "sobel filter 7  (of 12)"
filters.sobel(right[:,:,0],1,rx[:,:,0])
print "sobel filter 8  (of 12)"
filters.sobel(right[:,:,1],1,rx[:,:,1])
print "sobel filter 9  (of 12)"
filters.sobel(right[:,:,2],1,rx[:,:,2])
print "sobel filter 10 (of 12)"
filters.sobel(right[:,:,0],0,ry[:,:,0])
print "sobel filter 11 (of 12)"
filters.sobel(right[:,:,1],0,ry[:,:,1])
print "sobel filter 12 (of 12)"
filters.sobel(right[:,:,2],0,ry[:,:,2])
print "sobel filtering done."

# Save images representing all metainformation

