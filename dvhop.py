#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     03-09-2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import math
class DVHop:
    def __init__(self):
        self.R=20
        self.BorderLen=100
        self.NodeCount=100
        self.Ratio=0.2
##        self.NodeCoordinate=np.zeros((2,self.NodeCount))
##        for idx in range(2):
##            for inner in range(self.NodeCount):
##                self.NodeCoordinate[idx,inner]=np.floor(np.random.random())
        self.NodeCoordinate=np.floor(np.random.random((2,self.NodeCount))*self.BorderLen)
    def stepBroadcast(self):
        self.distMtx=np.zeros((self.NodeCount,self.NodeCount))
        for idx in range(self.NodeCount):
            for inner in range(self.NodeCount):
                self.distMtx[idx,inner]=math.sqrt(math.pow(self.NodeCoordinate[0,idx]-self.NodeCoordinate[0,inner],2)+math.pow(self.NodeCoordinate[1,idx]-self.NodeCoordinate[1,inner],2))
                self.distMtx[inner,idx]=self.distMtx[idx,inner]
        self.hopMtx=np.ones((self.NodeCount,self.NodeCount))*(1000)
        for idx in range(self.NodeCount):
            for inner in range(self.NodeCount):
                if self.distMtx[idx,inner]==0:
                    self.hopMtx[idx,inner]=0
                elif self.distMtx[idx,inner]<self.R:
                    self.hopMtx[idx,inner]=1
        for idxK in range(self.NodeCount):
            for idxI in range(self.NodeCount):
                for idxJ in range(self.NodeCount):
                    if self.hopMtx[idxI,idxJ]>self.hopMtx[idxI,idxK]+self.hopMtx[idxK,idxJ]:
                        self.hopMtx[idxI,idxJ]=self.hopMtx[idxI,idxK]+self.hopMtx[idxK,idxJ]
        print '*'*80
        print self.distMtx
    def stepCaculateAHS(self):
        self.AchorCount=int(math.floor(self.NodeCount*self.Ratio))
        self.UnknownCount=self.NodeCount-self.AchorCount
        self.AHS=np.zeros(self.AchorCount)
        for idx in range(self.AchorCount):
            sumDist=0
            sumHop=0
            for inner in range(self.AchorCount):
                sumDist=sumDist+self.distMtx[idx,inner]
                sumHop=sumHop+self.hopMtx[idx,inner]
            self.AHS[idx]=sumDist/sumHop
        print self.AHS
    def stepEstimatePosition(self):
        self.UnknownAHS=np.zeros(self.UnknownCount)
        for idx in range(self.AchorCount,self.NodeCount):
            minIdx=0
            minDist=self.distMtx[idx,0]
            for inner in range(1,self.AchorCount):
                if minDist>self.distMtx[idx,inner]:
                    minIdx=inner
                    minDist=self.distMtx[idx,inner]
            self.UnknownAHS[idx-self.AchorCount]=self.AHS[minIdx]
        print 'Unknown AHS'*20
        print self.UnknownAHS
        self.Un2AchorDistMtx=np.zeros((self.UnknownCount,self.AchorCount))
        for idx in range(self.AchorCount,self.NodeCount):
            for inner in range(self.AchorCount):
                self.Un2AchorDistMtx[idx-self.AchorCount,inner]=self.UnknownAHS[idx-self.AchorCount]*self.hopMtx[idx,inner]
        AMtx=np.zeros((self.AchorCount-1,2))
        BMtx=np.zeros(self.AchorCount-1)

        self.EstimateXYMtx=np.zeros((2,self.UnknownCount))
        for idxUn in range(self.UnknownCount):
            for idx in range(self.AchorCount-1):
                for inner in range(2):
                    AMtx[idx,inner]=self.NodeCoordinate[inner,idx]-self.NodeCoordinate[inner,self.AchorCount-1]
            AMtx=-2*AMtx
            for idx in range(self.AchorCount-1):
                BMtx[idx]=math.pow(self.Un2AchorDistMtx[idxUn,idx],2)-math.pow(self.Un2AchorDistMtx[idxUn,self.AchorCount-1],2)-math.pow(self.NodeCoordinate[0,idx],2)-math.pow(self.NodeCoordinate[1,idx],2)+math.pow(self.NodeCoordinate[0,self.AchorCount-1],2)+math.pow(self.NodeCoordinate[1,self.AchorCount-1],2)
            tmp=np.dot(np.dot(np.linalg.inv(np.dot(AMtx.T,AMtx)),AMtx.T),BMtx)
            self.EstimateXYMtx[0,idxUn]=tmp[0]
            self.EstimateXYMtx[1,idxUn]=tmp[1]
        print '%'*80
        print self.NodeCoordinate
        print '$'*80
        print self.EstimateXYMtx













    def showNode(self):
        plt.plot(self.NodeCoordinate[0,self.AchorCount:self.NodeCount],self.NodeCoordinate[1,self.AchorCount:self.NodeCount],'ro')
        plt.plot(self.EstimateXYMtx[0,:],self.EstimateXYMtx[1,:],'g*')
        plt.show()
    def test(self):
        print self.NodeCoordinate
def tstfun():
    dvh=DVHop()
    dvh.test()

    dvh.stepBroadcast()
    dvh.stepCaculateAHS()
    dvh.stepEstimatePosition()
    dvh.showNode()

def main():
    pass
    tstfun()

if __name__ == '__main__':
    main()
