import datetime
from itertools import takewhile
from itertools import dropwhile
def parse(row):
    arydate=strdate=row[0].split('-')
    year=int(arydate[0])
    month=int(arydate[1])
    day=int(arydate[2])
    return (datetime.date(year,month,day),float(row[1]),row[2],row[3])
class Expense:
    def __init__(self,dbname):
        with open(dbname) as fh:
            lines=fh.readlines()
        self.__db=list()
        for li in lines:
            if len(li.strip())==0:continue
            row=li.split()
            cnt=len(row)
            if cnt != 4:
                raise Exception(f'unexpect cols{cnt} in line[{li}]')
            self.__db.append(parse(row))
        self.__db.sort(key=lambda da:da[0],reverse=True)
    def save(self):
        print('details of lastmont')
        self.month(4)
    def search(self,scope=(datetime.date(2025,1,1),datetime.date.today()),tag=None):
        sumx=0
        for rec in takewhile(lambda x:x[0]>scope[0],dropwhile(lambda x:x[0]>=scope[1],self.__db)):
            if tag==None:
                print(f'{rec[0]} {rec[1]:8.2f} {rec[2]} {rec[3]}')
            else:
                if tag==rec[2]:
                    print(f'{rec[0]} {rec[1]:8.2f} {rec[2]} {rec[3]}')
            sumx = sumx + rec[1]
        print(f'total ￥{sumx:.2f}')
    def month(self,m=0,y=2026,tag=None):
        today=datetime.date.today()
        
        if m==0:
            sm=today.month
            if sm==1:
                sm=12
                syr=today.year-1
            else:
                sm=sm-1
                syr=today.year
        else:
            sm=m
            syr=y
        if sm==12:
            em=1
            eyr=syr+1
        else:
            em=sm+1
            eyr=syr
        scope=(datetime.date(syr,sm,1),datetime.date(eyr,em,1))
        print(f'{scope[0]}~{scope[1]}')
        self.search(scope,tag)
        
if __name__=="__main__":
    a=Expense('big-expense.txt')
    a.month(4)
