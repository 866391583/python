#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      libdzyl
#
# Created:     26-05-2014
# Copyright:   (c) libdzyl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def fibo(len):
    a=[0,1]
    for n in range(len-2):
        a.append(a[n]+a[n+1])
    return a

class Circle:
    def __init__(self,point,radius):
        self.radius=radius
        self.point=point
    def areaAndGirth(self):
        area=math.pi*pow(self.radius,2)
        girth=2*math.pi*self.radius
        return area,girth
    def printCircle(self):
        a,b=self.point
        print 'Point:[',a,b,']'
        area,girth=self.areaAndGirth()
        print 'Area:',area
        print 'Girth:',girth



def main():
    pass

if __name__ == '__main__':
    main()
