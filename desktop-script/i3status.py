#!/bin/python -u
### in case python output will be bufferred.
### use `python -u ` to avoid it in status_command
### 
import time
import json
import netadapt
import cpu
import battery
import mpv_ctrl
from other import fill


class statustime(dict):
    def update(self):
        now=time.time()
        tm=time.localtime(time.time())
        fill(self,time.strftime("%Y-%m-%d %X",tm),time.strftime("%X",tm),"#34aa45")

def version():
    print('{"version":1}')
if __name__ == "__main__":
    cols=(cpu.Cpu(),mpv_ctrl.MpvControl(),cpu.Mem(),netadapt.Net(),battery.Battery(),statustime())
    for idx in range(len(cols)):
        cols[idx]['name']='n{}'.format(idx)
    version()
    print('[')
    while(True):
        for col in cols:
            col.update()
        print(json.dumps(cols,ensure_ascii=False),end=",\n")
        time.sleep(5)
