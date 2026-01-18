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

img=iio.imread("cat_wizard.jpg")

#limit dimensions by image size
height=min(len(img), height)
width = min(len(img[0]), width)



def cToVal(c):
    val=0
    if isinstance(c, np.uint8):
        val= c/255
    else:
        a=255
        if len(c)>3:
            a=c[3]
        val= (c[0]/255+c[1]/255+c[2]/255)/3*(a/255)
    if not invert:
        val=1-val

    return val


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

print(img[0][0])
