# 1. IMG NEGETIVE
def image_negetive(im):
    L = 256
    pixelMapIn = im.load()
    out1 = im.copy()
    pixelMapOut = out1.load()
    for i in range (im.size[0]):
        for j in range(im.size[1]):
            r = pixelMapIn[i,j][0]
            pixelMapOut[i,j] = (int(L-1-r),pixelMapIn[i,j][1])
            
    out1.show("Image Negetive")