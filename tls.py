class mylist:
    def __init__(self,*list):
        self.list=[]
        for x in list:
            self.list.append(x)
    def setlist(self,list):
        self.list=list
    def printt(self):
        print 'mylist:',self.list
        
    def aver(self):
        sum=0.0
        for x in self.list:
            sum+=x
        return sum/len(self.list)
    def __sub__(self,num):
        res=[]
        for x in self.list:
            res.append(x-num)
        return res
    def __mul__(self,list):
        sum=0
        for x in range(len(self.list)):
            sum+=self.list[x]*list[x]
        return sum
if __name__=='__main__':
    myx=mylist(1,2,3,4,5,6,7,8,9,10)
    myy=mylist(1,2,2,4,4,8,9,10,12,13)
    xaver=myx.aver()
    yaver=myy.aver()
    xvec=mylist()
    xvec.setlist(myx-xaver)
    xvec.printt()
    yvec=mylist()
    yvec.setlist(myy-yaver)
    yvec.printt()
    xlist=myx-xaver
    ylist=myy-yaver
    print 'x*x',xvec*xlist
    print 'x*y',xvec*ylist
    print '(x*y)/(x*x)',(xvec*ylist)/(xvec*xlist)
    
