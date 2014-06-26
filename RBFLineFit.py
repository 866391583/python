#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dzylc
#
# Created:     26-06-2014
# Copyright:   (c) dzylc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
def service():
    t=np.arange(-9,9)
    y=t*np.sin(t)

    plt.plot(t,y,'ro')
    g=np.zeros((len(t),len(t)))
    for m in range(len(t)):
        for n in range(len(t)):
            g[m,n]=np.exp(-np.abs(t[m]-t[n]))

    w=np.dot(np.dot(np.linalg.inv(np.dot(g.T,g)),g.T),y)
    tt=np.arange(-9,9,0.01)
    g2=np.zeros((len(tt),len(t)))
    for m in range(len(tt)):
        for n in range(len(t)):
            g2[m,n]=np.exp(-np.abs(tt[m]-t[n]))
    yy=np.dot(g2,w)
    print tt
    print '/'*80
    print g2
    print '*'*80
    print yy
    line=tt*np.sin(tt)
    plt.plot(tt,line,'r')
    plt.plot(tt,yy)

    plt.show()
def main():
    pass
    service()

if __name__ == '__main__':
    main()
