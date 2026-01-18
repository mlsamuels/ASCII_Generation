import imageio.v2 as iio
import matplotlib.pyplot as plt
import math

import numpy as np

chars=[' ','.',',','-',':','/','=','+','%','&','$','X','@','H','M','#']

#define dimensions
width=40
height=int(0.4*width)

img=iio.imread("star.png")

#limit dimensions by image size
height=min(len(img), height)
width = min(len(img[0]), width)



def cToVal(c):
    if isinstance(c, np.uint8):
        return 1-c/255

    a=255
    if len(c)>3:
        a=c[3]
    return -(c[0]/255+c[1]/255+c[2]/255)/3*(a/255)


for i in range(0,height):
    for j in range(0, width):
        blockHeight = len(img)/height
        blockWidth = len(img[0])/width
        valSum=0
        for r in range(0,int(blockHeight)):
            for c in range(0,int(blockWidth)):
                color = img[int(i*blockHeight)+r][int(j*blockWidth)+c]
                valSum+=cToVal(color)
        valAvg=valSum/(int(blockHeight)*int(blockWidth))
        #print(valAvg)
        index = int(valAvg * len(chars))
        if index == len(chars):
            index -= 1
        char = chars[index]

        print(char, end="")
    print()


