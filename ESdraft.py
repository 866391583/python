#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dzylc
#
# Created:     24-06-2014
# Copyright:   (c) dzylc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import math
mu=50
children=350.0
mutate=7
sigma=1
class Seed:
    def __init__(self,xpoint,ypoint):
        self.xpoint=xpoint
        self.ypoint=ypoint
        self.flag=True
    def getValue(self):
        return self.xpoint*np.sin(4*math.pi*self.xpoint)+self.ypoint*np.sin(20*math.pi*self.ypoint)+21.5
    def __add__(self,sigmaxy):
        return Seed(self.xpoint+sigmaxy[0],self.ypoint+sigmaxy[1])
    def setFlase(self):
        self.flag=Flase

    def getX(self):
        return self.xpoint
    def getY(self):
        return self.ypoint
    def getFlag(self):
        return self.flag
def runcode():
    museed=[]
    for m in range(10):
        for n in range(5):
            tmpseed=Seed(np.random.rand()*1.24-0.3+1.24*m,np.random.rand()*0.34+4.1+0.34*n)
            museed.append(tmpseed)
    iterCount=100
    sigma=1
    for u in range(iterCount):
        successCount=0
        lamseed=[]
        for v in range(mutate):
            for w in range(mu):
                while True:
                    child=museed[w]+sigma*np.random.randn(2)
                    if child.getX()>-0.3 and child.getX()<12.1 and child.getY()>4.1 and child.getY()<5.8:
                        lamseed.append(child)
                        break
                if lamseed[-1].getValue()>museed[w].getValue():
                    successCount+=1
        if successCount/children>0.2:
            sigma=sigma*1.25
        else:
            sigma=sigma*0.82
        seedvalues=[]
        seedvalues2=[]
        for h in lamseed:
            seedvalues.append(h.getValue())
            seedvalues2.append(h.getValue())
        seedvalues.sort()
        seedvalues2=np.array(seedvalues2)
        lamseed=np.array(lamseed)
        museed=[]

        for k in range(mu):
            museed.append(lamseed[seedvalues[k]==seedvalues2][0])

        print museed[0].getValue(),'\t',museed[0].getX(),'\t',museed[0].getY()
        print u







##        for h in range(len(lamseed)):
##            #tmpchild=Seed()
##            for k in range(len(lamseed)-1):
##                print 'abc'










def main():
    pass
    runcode()
    print 'finished'

if __name__ == '__main__':
    main()
