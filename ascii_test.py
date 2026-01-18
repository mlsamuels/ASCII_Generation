import imageio.v2 as iio
import matplotlib.pyplot as plt
import math

import numpy as np

chars=[' ','.',',','-',':','/','=','+','%','&','$','X','@','H','M','#']

#define dimensions
width=170
height=int(0.4*width)

#invert
invert=False

img=iio.imread("star.png")

#limit dimensions by image size
height=min(len(img), height)
width = min(len(img[0]), width)


#convert from color to value on the range [0,1]
def cToVal(c):
    val=0
    #simple value
    if isinstance(c, np.uint8):
        val= c/255
    #array value
    else:
        #jpgs have no transparency
        a=255
        if len(c)>3:
            a=c[3]
        val= (c[0]/255+c[1]/255+c[2]/255)/3*(a/255)
    if not invert:
        val=1-val

    return val


#iterate over target dimensions
for i in range(0,height):
    for j in range(0, width):
        #define the block size used to calculate one 'pixel' of the final result
        blockHeight = len(img)/height
        blockWidth = len(img[0])/width

        #iterate within block to find the average color value
        valSum=0
        for r in range(0,int(blockHeight)):
            for c in range(0,int(blockWidth)):
                color = img[int(i*blockHeight)+r][int(j*blockWidth)+c]
                valSum+=cToVal(color)
        valAvg=valSum/(int(blockHeight)*int(blockWidth))

        #find which character to use from the average value
        index = int(valAvg * len(chars))
        #if the average value was 1, the index needs to go back 1
        if index == len(chars):
            index -= 1
        char = chars[index]

        #print character
        print(char, end="")

    #next line
    print()

