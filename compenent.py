class subklass:
    def __init__(self,list):
        self.list=list
    def printt(self):
        print 'list:',self.list
        
class klass:
    def __init__(self,compenent):
        self.compenent=compenent
    def printt(self):
        print 'compenent:',
        self.compenent.printt()
if __name__=='__main__':
    ls=range(10)
    sub=subklass(ls)
    kla=klass(sub)
    sub.printt()
    klass.printt(kla)
    ls.reverse()
    print '&'*80
    sub.printt()
    kla.printt()
        
