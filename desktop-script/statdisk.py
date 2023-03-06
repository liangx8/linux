import other

class StatDisk(dict):
    ''' read /proc/diskstats '''
    def __init__(self):
        with open('/proc/diskstats','r') as st:
            data=[]
            head=[]
            for li in st:
                row=li.split()
                nrow=[]
                for n in range(20):
                    nrow.append(int(n))
                data.append(nrow)
        
    def update(self):
        other.fill(self,"calcuting ...",None,None)
    def between(self):
        d2=stat()
        for rdx in range(len(d2)):
            for ix in range(3,20):
                d2[rdx][ix]=d2[rdx][ix] - self.__d1[rdx][ix]
        return d2
def stat():
    with open('/proc/diskstats','r') as st:
        data=[]
        for li in st:
            row=li.split()
            nrow=[]
            for n in row[3:]:
                nrow.append(int(n))
            data.append(nrow)
        return data
