import subprocess
import re
import json
from other import fill
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

class Net(dict):
    def __init__(self):
        self.__iface=guessNetInterface()
    def update(self):
        if not self.__iface:
            self.__iface=guessNetInterface()
        if self.__iface:
            try:
                with open('/sys/class/net/{}/statistics/rx_bytes'.format(self.__iface),'r') as rb:
                    r = rb.read()
                fill(self,"{}: {}".format(self.__iface,display_amount(int(r))),None,"#3466ee")
                return
            except:
                pass
        fill(m,"无网",None,"#eaeaea")
        return
            
        
        
