import os, numpy, PIL
from PIL import Image

# Access all files in the directory
allfiles = os.listdir(os.getcwd())
imlist = [filename for filename in allfiles if filename[-4:] in ['.jpg', '.JPG']]

# Determine dimensions of image and number of images
# In the case where images are different sizes this should be the min width and height
w, h = Image.open(imlist[0]).size
N = len(imlist)

# Create array of floats to store the image
arr = numpy.zeros((h, w, 3), numpy.float)

# Iterate through images, scale pixel values and add to output array
for im in imlist:
    imarr = numpy.array(Image.open(im), dtype = numpy.float)
    arr = arr + imarr / N

# Round values and cast as 8-bit int
arr = numpy.array(numpy.round(arr), dtype = numpy.uint8)

# Generate, save and preview final image
out = Image.fromarray(arr, mode = 'RGB')
out.save("average.png")
out.show()
