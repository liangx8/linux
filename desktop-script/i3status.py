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
import io
from other import fill


class statustime(dict):
    def __init__(self):
        self['background']='#bc4590'
    def update(self):
        now=time.time()
        tm=time.localtime(time.time())
        fill(self,time.strftime("%Y-%m-%d %X",tm),time.strftime("%X",tm),None)


def run(cols,log,logn):
    print('[')
    while(True):
        for col in cols:
            col.update()
        print(json.dumps(cols,ensure_ascii=False),end=",\n")
        if log.tell() > 0:
            logval=log.getvalue()
            log.seek(0)
            with open(logn,'a') as lf:
                lf.write(logval)
            log.truncate()
            
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
    print('{"version":1,"click_events":true}')
#    print('{"version":1}')
    
if __name__ == "__main__":
    version()
    cfgname=os.environ['HOME']+'/git/linux/desktop-script/i3status.cfg'
    cfg=config(cfgname)
    cfgerr=False
    logname='/tmp/sway-bar.log'
    if isinstance(cfg,Exception):
        cfgerr=True
    else:
        if 'log' in cfg:
            logname=cfg['log']
    log=io.StringIO()
    
    print('sway-bar log start',file=log)
    cols=(cpu.Cpu(),mpv_ctrl.MpvControl(),cpu.Mem(),netadapt.Net(),battery.Battery(),wallpaper.Wallpaper(cfg['wallpaper'],log),statustime())
    for idx in range(len(cols)):
        cols[idx]['name']='n{}'.format(idx)
    tak=threading.Thread(target=run,args=(cols,log,logname))
    tak.start()
    if cfgerr:
        print(f'open file {cfgname} error',file=log)
    #log.flush()
    cnt=0
    while True:
        line=sys.stdin.readline()
        # bug: 这里只执行了１次，以后就没有信息再进来了
        if len(line)<3:
            continue
        with open(logname,'a') as lf:
            lf.write(line)
        #print(line,file=log,end="")
        if line[0]==',':
            raw=line[1:]
        else:
            raw=line
        ev=json.load(raw)
        #print(f'{ev}',file=log)
        #log.flush()
