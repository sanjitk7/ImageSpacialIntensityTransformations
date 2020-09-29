from PIL import Image
from math import log10
import numpy as np
from image_negetive import image_negetive
from image_log_transform import image_log_transform
from image_gamma_powerlaw_transform import image_power_law_transform
from contrast_stretching import contrast_stretching
from image_graylevel_slicing import image_graylevel_slicing
from image_bitplane_slicing import bit_plane_splicing

im = Image.open("pic.png").convert("LA")


print("Enter your preffered Operation:\n1.Image Negetive\n2.Log Transform\n3.Power-Law Transform\n4.Contrast Stetching\n5.Graylevel Sclicing\n6.Bit Plane Splicing")
selection = int(input())

if (selection == 1):
    # SPACIAL IMAGE OPERATIONS - SINGLE PIXEL OPERATIONS
    # 1. IMG NEGETIVE
    print("Formula: s=L-1-r")
    image_negetive(im)
elif (selection == 2):
    # 2. LOG TRANSFORMS
    c = int(input("Enter c value:"))
    print("Formula: s=c*log(1+r)")
    image_log_transform(im)
elif(selection==3):
    # 3. POWER-LAW TRANSFORMATIONS
    c = int(input("Enter c value:"))
    gamma = int(input("Enter Gamma value:"))
    print("Formula: s=c*r**gamma")
    image_power_law_transform(im,c,gamma)
elif (selection==4):
    # PIECE WISE OPERATIONS 
    # 1. CONTRAST STRETCHING
    r1,s1,r2,s2 = map(int,input("Enter r1, s1, r2, s2 values (with spaces):").split())
    print("Note for binary image converstion use r1=r2")
    print("Formula: s=(r-r1)*((s2-s1)/(r2-r1))+r1")
    contrast_stretching(im,r1,s1,r2,s2)
elif (selection==5):
    # 2. GRAYLEVEL SLICING
    A, B = map(int, input("Enter lower and upper limits:").split())
    S = int(input("Enter S value (conv):"))
    if (input("Enter 'y' if background substitution is required:")=='y'):
        with_bg_subsititution = True
    else:
        with_bg_subsititution = False
    some_val_bg = int(input("Enter value to clip the background to:"))
    image_graylevel_slicing(im,with_bg_subsititution,some_val_bg,A,B,S)
elif (selection==6):
    # 3. BITPLANE SLICING
    bitPlaneNumber = int(input("Enter the bitplane number to obtain"))
    bit_plane_splicing(im,bitPlaneNumber)
