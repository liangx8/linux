import other
import os
statePath="/sys/class/power_supply/BAT1/uevent"
class Battery(dict):
    def __init__(self):
        other.fill(self,"caculating",None,"#aa0000")
        self['background']='#50ea23'
    def update(self):
        stat='N/A'
        try:
            with open(statePath,"r") as bf:
                d=data(bf)
                if d[2]=='Charging':
                    stat='C'
                else:
                    stat='D'
                # full/design 电池的健康值，最高电量/设计电量
                other.fill(self,"{}:{}%[{}%]".format(stat,d[3],int(d[0]/d[1]*100)),None,None)

        except:
            other.fill(self,"\uf0e7电源",'短文本',"#aa0000")
            return
x = ("POWER_SUPPLY_CHARGE_FULL_DESIGN","POWER_SUPPLY_CHARGE_FULL","POWER_SUPPLY_STATUS","POWER_SUPPLY_CAPACITY")
def data(fh):
    full=0
    design=0
    charging='N/A'
    capacity=0
    for line in fh:
        a,b=line.split('=')[:2]
        if a==x[0]:
            design=int(b)
        if a==x[1]:
            full=int(b)
        if a==x[2]:
            charging=b[:len(b)-1]
        if a==x[3]:
            capacity=int(b)
    return (full,design,charging,capacity)
def findBattery():
    try:
        with open(statePath,"r") as bf:
            print(data(bf))
    except Exception as e:
        print(e)

    

    
