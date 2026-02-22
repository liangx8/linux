#!/bin/python -u
### in case python output will be bufferred.
### use `python -u ` to avoid it in status_command
### 
import threading
import sys
import time
import json
import netadapt
import cpu
import battery
import mpv_ctrl
import wallpaper
from other import fill


class statustime(dict):
    def __init__(self):
        self['background']='#bc4590'
    def update(self):
        now=time.time()
        tm=time.localtime(time.time())
        fill(self,time.strftime("%Y-%m-%d %X",tm),time.strftime("%X",tm),None)


def run(logout):
    cols=(cpu.Cpu(),mpv_ctrl.MpvControl(),cpu.Mem(),netadapt.Net(),battery.Battery(),wallpaper.Wallpaper('/home/com/wallpaper/',logout),statustime())
    for idx in range(len(cols)):
        cols[idx]['name']='n{}'.format(idx)
    version()
    print('[')
    while(True):
        for col in cols:
            col.update()
        print(json.dumps(cols,ensure_ascii=False),end=",\n")
        time.sleep(5)

def version():
#    要sway-bar响应鼠标事件，要修改以下内容
#    print('{"version":1,"click_events":true}')
    print('{"version":1}')
    
if __name__ == "__main__":
    logname='/tmp/swb-input.log'
    with open(logname,'w',buffering=1) as log:
        tak=threading.Thread(target=run,args=(log,))
        tak.start()
        print('sway-bar log start',file=log)
        #log.flush()
        cnt=0
        while True:
            for line in sys.stdin:
                print(line,file=log)
                #log.flush()
            print(cnt,file=log)
            cnt = cnt + 1
            time.sleep(0.5)
