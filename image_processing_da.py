from PIL import Image
from math import log10
import numpy as np

im = Image.open("pic.png").convert("LA")
pixelMap = im.load()

out1 = im.copy()
pixelMap1 = out1.load()

out2 = im.copy()
pixelMap2 = out2.load()

out3 = im.copy()
pixelMap3 = out3.load()

# im.show()
# print(pixelMap[200,200])


# Listing All The pixel Values of the Image
for i in range (im.size[0]):
    for j in range(im.size[1]):
        print("f(" + str(i) + "," + str(j)+") = " + str(pixelMap[i,j][0]))


# SPACIAL IMAGE OPERATIONS - SINGLE PIXEL OPERATIONS

# 1. IMG NEGETIVE

for i in range (im.size[0]):
    for j in range(im.size[1]):
        pixelMap1[i,j] = (int(256-1-pixelMap[i,j][0]),pixelMap[i,j][1])
        # print(pixelMap[i,j])
out1.show("Image Negetive")
        
# 2. LOG TRANSFORMS

for i in range (im.size[0]):
    for j in range(im.size[1]):
        pixelMap2[i,j] = (int(40*np.log(1 + pixelMap[i,j][0])),pixelMap[i,j][1])
        # print(pixelMap[i,j])
out2.show("Log Transform")

# 3. POWER-LAW TRANSFORMATIONS

gamma = 4
c = 1
for i in range (im.size[0]):
    for j in range(im.size[1]):
        pixelMap3[i,j] = (int(c*255*(pixelMap[i,j][0]/255)**(1/gamma)),pixelMap[i,j][1])
out3.show("Power-Law Transform")


out4 = im.copy()
pixelMap4 = out4.load()

# PIECE WISE OPERATIONS 
# 1. CONTRAST STRETCHING

r1,s1,r2,s2 = 50,60,150,180
# r1,s1,r2,s2 = 49,1,50,255 (Binary Image (Theresholding Range))


for i in range(im.size[0]):
    for j in range (im.size[1]):
        r = pixelMap[i,j][0]
        pixelMap4[i,j] = (int((r-r1)*(s2-s1)/(r2-r1))+s1,pixelMap[i,j][1])
out4.show("Contrast Stretching")


out5 = im.copy()
pixelMap5 = out5.load()
# 2. GRAYLEVEL SLICING

with_bg_subsititution = False
A,B = 100,130
S = 170
some_val_bg = 50

for i in range (im.size[0]):
    for j in range(im.size[1]):
        r = pixelMap[i,j][0]
        if (r>=A and r<=B):
            pixelMap5[i,j] = (S,pixelMap[i,j][1])
        elif(with_bg_subsititution):
            pixelMap5[i,j] = (r,pixelMap[i,j][1])
        else:
            pixelMap5[i,j] = (some_val_bg,pixelMap[i,j][1])

im.show()
out5.show("Graylevel Slicing")


out6 = im.copy()
pixelMap6 = out6.load()
# 3. BITPLANE SLICING

bitPlaneNumber = 8
bitPlaneIndex = 8-bitPlaneNumber
bitPlane = np.array([])
multiplication_factor = 2**(bitPlaneNumber-1)
for i in range(im.size[0]):
    for j in range (im.size[1]):
        r = pixelMap[i,j][0]
        bin_r = np.binary_repr(r,width=8)
        # print("r,bin_r:",r,bin_r[bitPlaneNumber])
        pixelMap6[i,j] = (int(bin_r[bitPlaneIndex])*multiplication_factor,pixelMap[i,j][1])
        

im.show()
out6.show()
