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
        self.__db=[]
        for li in lines:
            row=li.split()
            cnt=len(row)
            if cnt != 4:
                raise Exception(f'unexpect cols{cnt} in line[{li}]')
            self.__db.append(parse(row))
    def save(self):
        for rec in self.__db:
            print(f'{rec[0]} {rec[1]:8.2f} {rec[2]} {rec[3]}')
            
if __name__=="__main__":
    a=Expense('big-expense.txt')
    a.save()
    
