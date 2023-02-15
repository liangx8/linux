### in case python output will be bufferred.
### use in i3bar with python -u prg.py
### 
#!/bin/python -u
import datetime
import time
import subprocess
import re
import time
import json
def guessNetInterface():
    r=subprocess.run(['ip','a'],stdout=subprocess.PIPE)
    if r.returncode != 0 :
        print(r.stderr)
        return
    bs=bytes(r.stdout)
    cpm=re.compile('''^(\d): (\w+): .+state UP group''')
    for bl in bs.splitlines():
        l=bl.decode()
        m=cpm.match(l)
        if m :
            return m.group(2)
    return None

def display_amount(size):
    if size > 10 * 1024 * 1024 * 1024:
        num = int(size / 1024/1024/1024)
        uom = 'G'
    elif size > 1024*1024:
        num = int(size / 1024 /1024)
        uom = 'M'
    elif size>1024:
        num = int(size / 1024)
        uom='K'
    else :
        num=size
        uom='b'
    return "{}{}".format(num,uom)
def fill(obj,ft,st,color):
    if ft :
        obj["full_text"]=ft
    if st:
        obj["short_text"]=st
    if color:
        obj["color"]=color
def version():
    print('{"version":1}')
if __name__ == "__main__":
    iface=guessNetInterface()
    version()
    print('[')
    print('[]')
    m1={}
    m2={}
    a=(m1,m2)
    ethPath='/sys/class/net/{}/statistics/rx_bytes'.format(iface)
    while(True):
        now=time.time()
        tm=time.localtime(now)
        if iface:
            with open(ethPath,'r') as rb:
                r = rb.read()
            amt=display_amount(int(r))
            fill(m1,"{}: {}".format(iface,amt),"{}".format(amt),"#ae4522")
            fill(m2,time.strftime("%Y-%m-%d %X",tm),time.strftime("%X",tm),"#55aaff")
            
            print(",",json.dumps(a))
        else:
            print("找不到网卡")
        time.sleep(5)
