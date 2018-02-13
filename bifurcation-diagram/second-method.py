from numpy import *
from pylab import *
from math import *
from PIL import Image

def logistica(x0,b,n):
    imgx = 1000
    imgy = 500
    image = Image.new("RGB", (imgx, imgy))

    P = linspace(2.5,4,imgx)

    for a in P:
        x = x0
        for j in range(n):
            x = x * (a - b*x)
            if j > n/2:
                image.putpixel((int(floor((imgx-1)*(a-2.5)/1.5)), int(floor(b*imgy*x/4))), (255, 255, 255))

    image.save("Bifurcation.png", "PNG")