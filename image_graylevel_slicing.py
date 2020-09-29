# 2. GRAYLEVEL SLICING

def image_graylevel_slicing(im,with_bg_subsititution,some_val_bg,A,B,S):
    pixelMapIn = im.load()
    out1 = im.copy()
    pixelMapOut = out1.load()
    for i in range (im.size[0]):
        for j in range(im.size[1]):
            r = pixelMapIn[i,j][0]
            if (r>=A and r<=B):
                pixelMapOut[i,j] = (S,pixelMapIn[i,j][1])
            elif(with_bg_subsititution):
                pixelMapOut[i,j] = (r,pixelMapIn[i,j][1])
            else:
                pixelMapOut[i,j] = (some_val_bg,pixelMapIn[i,j][1])
    out1.show()