import datetime
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
        sum=0
        for rec in self.__db:
            print(f'{rec[0]} {rec[1]:8.2f} {rec[2]} {rec[3]}')
            sum = sum + rec[1]
        print(f'total ￥{sum:.2f}')
    def search(self,scope=(datetime.datetime(2025,1,1),datetime.datetime.now())):
        pass
if __name__=="__main__":
    a=Expense('big-expense.txt')
    a.save()
    
