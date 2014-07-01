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
import numpy as np
import scipy.linalg as la
from scipy.optimize import fsolve

def service():
    a=np.array([[2,1],[1,2]])
    b=np.array([5,5])
    x=la.solve(a,b)
    print x
def service2(x):
    x0=float(x[0])
    x1=float(x[1])
    return [x0+x1-5,x0*x1-6.001]

def main():
    pass
    service()
    result=fsolve(service2,[5,7])
    print result
    print service2(result)


if __name__ == '__main__':
    main()
