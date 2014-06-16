class overload:
    def __init__(self,list):
        self.list=list
    def __add__(self,num):
        print '__add__'
        res=[]
        for x in self.list:
            res.append(x+num)
        return res
    def __radd__(self,num):
        print '__radd__'
        res=[]
        for x in self.list:
            res.append(x+num)
        return res
if __name__=='__main__':
    list=range(10)
    ol=overload(list)
    ls=ol+1
    print ls
    ls=2+ol
    print ls
    list[5]=20
    ls=2+ol
    print ls
