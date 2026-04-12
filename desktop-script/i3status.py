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
import mylog
from other import fill


class statustime(dict):
    def __init__(self):
        self['background']='#bc4590'
    def update(self):
        now=time.time()
        tm=time.localtime(time.time())
        fill(self,time.strftime("%Y-%m-%d %X",tm),time.strftime("%X",tm),None)


def showout(cols,log,logn):
    version()
    print('[')
    while(True):
        for col in cols:
            col.update()
        print(json.dumps(cols,ensure_ascii=False),end=",\n")
        log.flush()
        time.sleep(5)
def eventhdl(log):
    cnt=0
    while True:
        line=sys.stdin.readline()
        if len(line)<3:
            continue
        log.info(line)
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
    cfgname=os.environ['HOME']+'/git/linux/desktop-script/i3status.cfg'
    cfg=config(cfgname)
    cfgerr=False
    logname='/tmp/sway-bar.log'
    if isinstance(cfg,Exception):
        cfgerr=True
    else:
        if 'log' in cfg:
            logname=cfg['log']
    log=mylog.Log(logname)
    log.info('sway-bar log start')
    cols=(cpu.Cpu(),mpv_ctrl.MpvControl(),cpu.Mem(),netadapt.Net(),battery.Battery(),wallpaper.Wallpaper(cfg['wallpaper'],log),statustime())
    for idx in range(len(cols)):
        cols[idx]['name']='n{}'.format(idx)
    tak=threading.Thread(target=eventhdl,args=(log,))
    tak.start()
    if cfgerr:
        log.info(f'open file {cfgname} error')
    showout(cols,log,logname)
    #log.flush()
