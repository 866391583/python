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
import scipy as sc
import matplotlib.pyplot as plt
def main():
    pass
    t=np.arange(0,99,1)
    un=10*np.sin(0.5*t)
    plt.plot(t,un)
    plt.show()




##    x=np.arange(0,2*np.pi,0.01)
##    y=np.sin(x)
##    line=plt.plot(x,y,'m:',lw=5)
##    plt.legend(line,['Sin Function'])
##    plt.annotate('Sin Function',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.05))
##    plt.ylim(-2,2)
##    plt.grid(True)
##    plt.show()
##def LMS(xn,dn,M,mu,yn):
##    wArr=np.zeros([M,1])
##    wn=np.matrix(wArr)
##    for e in range(M-1,len(xn)):
##        subx=xn[e:-1:e-M+1]
##        y=(wn.T)*subx
##        error=dn[e]-y
##        wn=wn+2*mu*error*subx
##    for f in range(M-1,len(xn)):
##        subx=xn[f:-1:f-M+1]
##        yn[f]=(wn.T)*subx


def multiVector(A,B):
    C=sc.zeros(len(A))
    for i in range(len(A)):
        C[i]=A[i]*B[i]
    return sum(C)
def inVector(A,b,a):
    D=sc.zeros(b-a+1)
    for i in range(b-a+1):
        D[i]=A[i+a]
    return D[::-1]
def LMS(xn,dn,M,mu,itr):
    en=sc.zeros(itr)
    W=[[0]*M for i in range(itr)]
    for k in range(itr)[M-1:itr]:
        x=inVector(xn,k,k-M+1)
        y=multiVector(W[k-1],x)
        en[k]=dn[k]-y
        W[k]=np.add(W[k-1],2*mu*en[k]*x)
    yn=sc.inf*sc.ones(len(xn))
    for k in range(len(xn))[M-1:len(xn)]:
        x=inVector(xn,k,k-M+1)
        yn[k]=multiVector(W[len(W)-1],x)
    return (yn,en)




if __name__ == '__main__':
    itr=1000 #采样的点数
    M=5 #滤波器的阶数
    mu=3.0342e-005 #步长因子
    t=np.linspace(0,99,itr)
    xs=10*np.sin(0.5*t)
    xn1=sc.randn(itr) #参考输入端的输入信号
    xn=np.add(xn1,xs) #原始输入端的信号为被噪声污染的正弦信号
    dn=xs #对于自适应对消器，用dn作为期望
    (yn,en)=LMS(xn,dn,M,mu,itr)
    plt.figure(1)
    plt.plot(t,xn,label="$xn$")
    plt.plot(t,dn,label="$dn$")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("original signal xn and desired signal dn")
    plt.legend()
    plt.figure(2)
    plt.plot(t,dn,label="$dn$")
    plt.plot(t,yn,label="$yn$")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("original signal xn and processing signal yn")
    plt.legend()
    plt.figure(3)
    plt.plot(t,en,label="$en$")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("error between processing signal yn and desired voltage dn")
    plt.legend()
    plt.show()
    main()

