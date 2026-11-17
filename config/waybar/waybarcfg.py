import tomllib
import re
import os
def transfer(cfg):
    for key in cfg:
        val=cfg[key]
        if isinstance(val,dict):
            transfer(val)
            return
        if isinstance(val,str):
            val1=re.sub(r'{home}',os.environ['HOME'],val)
            cfg[key]=val1
            return

def loadcfg(ininame):
    with open(ininame,"rb") as inif:
        cfg=tomllib.load(inif)
        transfer(cfg)
    return cfg
        
if __name__=='__main__':
    ini=loadcfg('/home/ram/ini.toml')
    print(ini)
