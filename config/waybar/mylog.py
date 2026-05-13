import datetime
class WaybarLog:
    def __init__(self,logn):
        self.__logn=logn
    def info(self,msg):
        with open(self.__logn,'a') as hdl:
            print(f"{datetime.datetime.now():%Y-%m-%d %X}",msg,file=hdl)