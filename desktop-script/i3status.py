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
import os
from other import fill


class statustime(dict):
    def __init__(self):
        self['background']='#bc4590'
    def update(self):
        now=time.time()
        tm=time.localtime(time.time())
        fill(self,time.strftime("%Y-%m-%d %X",tm),time.strftime("%X",tm),None)


def run(logout,cfg):
    cols=(cpu.Cpu(),mpv_ctrl.MpvControl(),cpu.Mem(),netadapt.Net(),battery.Battery(),wallpaper.Wallpaper(cfg['wallpaper'],logout),statustime())
    for idx in range(len(cols)):
        cols[idx]['name']='n{}'.format(idx)
    version()
    print('[')
    while(True):
        for col in cols:
            col.update()
        print(json.dumps(cols,ensure_ascii=False),end=",\n")
        time.sleep(5)
def config(cfgname):
    try:
        with open(cfgname) as cfg:
            lines=cfg.readlines()
    except Exception as e:
        return e
    cfg={}
    for li in lines:
        key,val=li.split('=')
        cfg[key]=val.strip()
    return cfg
def version():
#    要sway-bar响应鼠标事件，要修改以下内容
#    print('{"version":1,"click_events":true}')
    print('{"version":1}')
    
if __name__ == "__main__":
    cfgname=os.environ['HOME']+'/git/linux/desktop-script/i3status.cfg'
    cfg=config(cfgname)
    cfgerr=False
    if isinstance(cfg,Exception):
        logname='/tmp/sway-bar.log'
        cfgerr=True
    else:
        if 'log' in cfg:
            logname=cfg['log']
        else:
            logname='/tmp/sway-bar.log'
    with open(logname,'w',buffering=1) as log:
        tak=threading.Thread(target=run,args=(log,cfg))
        tak.start()
        print('sway-bar log start',file=log)
        if cfgerr:
            print(f'open file {cfgname} error',file=log)
        #log.flush()
        cnt=0
        while True:
            for line in sys.stdin:
                print(line,file=log)
                #log.flush()
            print(cnt,file=log)
            cnt = cnt + 1
            time.sleep(0.5)
