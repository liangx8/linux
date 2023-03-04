#!/bin/python -u
### in case python output will be bufferred.
### use `python -u ` to avoid it in status_command
### 
import time
import json
import netadapt
import cpu
from other import fill


class statustime(dict):
    def update(self):
        now=time.time()
        tm=time.localtime(time.time())
        netadapt.fill(self,time.strftime("%Y-%m-%d %X",tm),time.strftime("%X",tm),"#34aa45")
        self['background']="#eaeaea"


def version():
    print('{"version":1}')
if __name__ == "__main__":
    rows=(cpu.Mem(),cpu.Cpu(),netadapt.Net(),statustime())
    version()
    print('[')
    while(True):
        for row in rows:
            row.update()
        print(json.dumps(rows,ensure_ascii=False),end=",\n")
        time.sleep(5)
