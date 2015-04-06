# Input: 'in.png'
# Output: 'out.png' gradient magnitude of 'in.png'
from numpy import *
from PIL import Image
from scipy.ndimage import filters
image = 'in.png'
im = array(Image.open(image).convert('L'))

imx = zeros(im.shape)
filters.sobel(im,1,imx)
imy = zeros(im.shape)
filters.sobel(im,0,imy)
grad= sqrt(imx**2+imy**2)

out = Image.fromarray(uint8(grad))
out.save('out.png')
