# 3. POWER-LAW TRANSFORMATIONS
def image_power_law_transform(im,c=1,gamma=4):
    pixelMapIn = im.load()
    out1 = im.copy()
    pixelMapOut = out1.load()
    for i in range (im.size[0]):
        for j in range(im.size[1]):
            r = pixelMapIn[i,j][0]
            pixelMapOut[i,j] = (int(c*255*((r/255)**(1/gamma))),pixelMapIn[i,j][1])
    out1.show()