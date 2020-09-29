def contrast_stretching(im,r1,s1,r2,s2):
    pixelMapIn = im.load()
    out1 = im.copy()
    pixelMapOut = out1.load()
    for i in range(im.size[0]):
        for j in range (im.size[1]):
            r = pixelMapIn[i,j][0]
            if (r1!=r2):
                pixelMapOut[i,j] = (int((r-r1)*(s2-s1)/(r2-r1))+s1,pixelMapIn[i,j][1])
            else:
                pixelMapOut[i,j] = (int((r-r1)*(s2-s1))+s1,pixelMapIn[i,j][1])
    out1.show("Contrast Stretching")