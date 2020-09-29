import numpy as np

# 2. LOG TRANSFORMS
def image_log_transform(im,c):
    pixelMapIn = im.load()
    out1 = im.copy()
    pixelMapOut = out1.load()
    for i in range (im.size[0]):
        for j in range(im.size[1]):
            r = pixelMapIn[i,j][0]
            pixelMapOut[i,j] = (int(c*np.log(1 + r)),pixelMapIn[i,j][1])
            # print(pixelMap[i,j])
    out1.show("Log Transform")