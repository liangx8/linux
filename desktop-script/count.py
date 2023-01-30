#!/bin/python
import datetime
import time
import subprocess
import re
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

if __name__ == "__main__":
    iface=guessNetInterface()
    if iface:
        with open('/sys/class/net/{}/statistics/rx_bytes'.format(iface),'r') as rb:
            r = rb.read()
        print(iface+":",display_amount(int(r)))
    else:
        print("找不到网卡")

