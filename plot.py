#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      libdzyl
#
# Created:     09-05-2014
# Copyright:   (c) libdzyl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
def main():
    pass
    x=np.arange(0,2*np.pi,0.01)
    y=np.sin(x)
    line=plt.plot(x,y,'m:',lw=5)
    plt.legend(line,['Sin Function'])
    plt.annotate('Sin Function',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.05))
    plt.ylim(-2,2)
    plt.grid(True)
    plt.show()
if __name__ == '__main__':
    main()
