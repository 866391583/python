def funkeydefault(b,a=[1,2,3]):
    print 'list',a
    for x in b.keys():
        print x,'=>',b[x]
def funtuple(*tup):
    print '&'*3,'*tuple','*'*8
    print tup
def fundict(**dict):
    print '&'*8,'**dict','&'*8
    for x in dict:
        print x,'=>',dict[x]
        
if __name__=='__main__':
    ls=range(10)
    dict={'a':1,'b':2}
    funkeydefault(b=dict)    
    funtuple(1,2,3)
    fundict(a=1,b=2)
    
