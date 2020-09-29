import numpy as np

# BIT PLANE SPLICING

def bit_plane_splicing(im,bitPlaneNumber):
    pixelMapIn = im.load()
    out1 = im.copy()

    pixelMapOut = out1.load()
    bitPlaneIndex = 8-bitPlaneNumber
    multiplication_factor = 2**(bitPlaneNumber-1)
    for i in range(im.size[0]):
        for j in range (im.size[1]):
            r = pixelMapIn[i,j][0]
            bin_r = np.binary_repr(r,width=8)
            # print("r,bin_r:",r,bin_r[bitPlaneNumber])
            pixelMapOut[i,j] = (int(bin_r[bitPlaneIndex])*multiplication_factor,pixelMapIn[i,j][1])
    out1.show()