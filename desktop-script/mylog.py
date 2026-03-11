import datetime
import io
class Log:
    def __init__(self,logobj):
        self.__logobj=logobj
        self.__log=io.StringIO()
    def info(self,msg):
        print(f"{datetime.datetime.now():%Y-%m-%d %X}",msg,file=self.__log)
    def flush(self):
        log=self.__log
        if log.tell() > 0:
            logv=log.getvalue()
            log.seek(0)
            if isinstance(self.__logobj,io.Writer):
                self.__logobj.write(logv)
            if isinstance(self.__logobj,str):
                with open(self.__logobj,'a') as lf:
                    lf.write(logv)
            log.truncate()
if __name__ == "__main__":
    import sys
    log=Log(sys.stdout)
    log.info("abcdeeeeee")
    log.flush()
