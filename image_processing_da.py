from PIL import Image
from math import log10
import numpy as np

im = Image.open("pic.png").convert("LA")
pixelMap = im.load()
# im.show()
# print(pixelMap[200,200])


# Listing All The pixel Values of the Image
# for i in range (im.size[0]):
#     for j in range(im.size[1]):
#         print("f(" + str(i) + "," + str(j)+") = " + str(pixelMap[i,j][0]))


# SPACIAL IMAGE OPERATIONS - SINGLE PIXEL OPERATIONS

# # 1. IMG NEGETIVE

# # for i in range (im.size[0]):
# #     for j in range(im.size[1]):
# #         pixelMap[i,j] = (int(256-1-pixelMap[i,j][0]),pixelMap[i,j][1])
# #         # print(pixelMap[i,j])
# # im.show()
        
# # # 2. LOG TRANSFORMS

# # for i in range (im.size[0]):
# #     for j in range(im.size[1]):
# #         pixelMap[i,j] = (int(40*np.log(1 + pixelMap[i,j][0])),pixelMap[i,j][1])
# #         # print(pixelMap[i,j])
# im.show()

# 3. POWER-LAW TRANSFORMATIONS

gamma = 4
c = 1
for i in range (im.size[0]):
    for j in range(im.size[1]):
        pixelMap[i,j] = (int(c*255*(pixelMap[i,j][0]/255)**(1/gamma)),pixelMap[i,j][1])
im.show()
