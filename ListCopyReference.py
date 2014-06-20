#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dzylc
#
# Created:     20-06-2014
# Copyright:   (c) dzylc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
def main():
    pass
    arr=np.array([1,2,3])
    print dir(arr)
    print 'arr'
    arr=np.array(([1,2,3],[1,2,5],(5,5,5)))
    print arr,arr.dtype
    ze=np.ones((18,18))
    print ze
    arr=np.linspace(0,10,20)
    print arr
    ind=np.indices((5,5,5))
    print ind
    ls=[[1,2,3],[1,4,3],[5,5,7]]
    print ls
    abc=ls[0:2]
    print abc
    '''key'''
    abc[0][0:2]=55,66
    #abc[0]=55
    '''key'''


    print abc
    print ls

if __name__ == '__main__':
    main()
