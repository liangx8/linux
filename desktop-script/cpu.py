import time
import other
import io
# 参考man proc 查找/proc/stat
class Cpu(dict):
    def __init__(self):
        _,self.__last=data()
    def update(self):
        names,cur = data()
        cnt=len(names)
#        totals=list(range(cnt))
#        avls=list(range(cnt))
        try:
            with io.StringIO() as buf:
                for idx in range(cnt):
                    total=0
                    avl=0
                    print(names[idx].upper(),end=":",file=buf)
                    
                    for ix in range(4):
                        total=total+cur[idx][ix]-self.__last[idx][ix]
                        
                        if ix<3:
                            avl=avl+cur[idx][ix]-self.__last[idx][ix]
                    print("{:02}".format(int(avl * 100 /total)),end=' ',file=buf)
                    #print("{}/{}".format(avl,total),end=' ',file=buf)
                    other.fill(self,buf.getvalue(),None,None)
        except:
            other.fill(self,"calcuting ...",None,"#00ff00")
        self.__last=cur

def data():
    aa=list()
    rownames=list()
    with open('/proc/stat','r') as st:
        for li in st:
            sa=li.split()
            if sa[0][:3]=='cpu':
                rownames.append(sa[0])
                a=list()
                for s in sa[1:]:
                    a.append(int(s))
                aa.append(a)
    return rownames,aa
            
def stat():
    #title=('user','nice','system','idle','iowait','irq','softirq','steal','guest','guest_nice')
    title=('user','nice','system','idle','iowait','irq','softirq','total')
    names,a1=data()
    
    time.sleep(1)
    _,a2=data()
    print('\t',end='')
    for t in title:
        print(t,end='\t')
    print()
    for idx in range(5):
        print(names[idx],end='\t')
        total=0
        for ix in range(7):
            old=a1[idx][ix]
            x=a2[idx][ix]-old
            total=total+x
            print(x,end='\t')
        print(total)
            

