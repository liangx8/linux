import pathlib
class Counter:
    def __init__(self,name):
        self.__fname=name
    def valueBeforeDec(self):
        fn=pathlib.Path(self.__fname)
        if fn.exists():
            with open(self.__fname) as cntf:
                line=cntf.readline()
                try:
                    cnt=int(line)
                except:
                    cnt=0
        else:
            cnt=0
        if cnt==0:
            self.setValue(0xffff)
        else:
            self.setValue(cnt-1)
        return cnt
    def setValue(self,val):
        with open(self.__fname,'w') as cntf:
            cntf.write(f'{val}')

