# Listing All The pixel Values of the Image

def list_all_pixels(im):
    for i in range (im.size[0]):
    for j in range(im.size[1]):
        print("f(" + str(i) + "," + str(j)+") = " + str(pixelMap[i,j][0]))