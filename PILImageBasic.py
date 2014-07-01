#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dzylc
#
# Created:     01-07-2014
# Copyright:   (c) dzylc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import Image
def service():
    im=Image.open('lena24.jpg')
    row,col=im.size
    print im.size,im.mode,im.format
    plt.subplot(211)
    plt.imshow(im,cmap=plt.cm.gray)
    plt.axis('off')
    for m in range(row):
        for n in range(col):
            im.putpixel((m,n),(tuple(255-np.array(im.getpixel((m,n))))))
    plt.subplot(212)
    plt.imshow(im,cmap=plt.cm.gray)
    plt.axis('off')
    plt.show()
def main():
    pass
    service()

if __name__ == '__main__':
    main()
