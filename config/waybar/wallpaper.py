import io
import json
import pathlib
import random
import subprocess
import os
import mylog
import counter



def loadCfg(path):
    ini=dict()
    with open(path) as cfgh:
        lines=cfgh.readlines()
    for line in lines:
        key,value=[item.strip() for item in line.split('=',1)]
        #print(key,value)
        idx=value.find('{home}')
        if idx<0:
            ini[key]=value
        else:
            os.environ['HOME']
            nv=value[:idx]+ os.environ['HOME'] + value[idx+6:]
            ini[key]=nv
    return ini
    
def listFiles(path):
    cb = lambda x:path+x.name
    pn=pathlib.Path(path)
    if pn.exists():
        return [cb(x) for x in pn.iterdir() if x.name.endswith('.png') or x.name.endswith('.jpg')]
    else:
        return None
def newList(path,fn,logf):
    conts=listFiles(path)
    if conts==None:
        logf.info(f'读取目录{path}中到图片列表出错')
        return None
    logf.info("新列表")
    random.shuffle(conts)
    total=len(conts)
    headcont=[f"1,{total+1}"]+conts
    with fn.open('w') as lf:
        for x in headcont:
            lf.write(x)
            lf.write('\n')
    return conts[0]


def loadPic(path,logf):
    fn=pathlib.Path(path+'pic-list.txt')
    if fn.exists():
        with fn.open() as lf:
            headcont=lf.readlines()
        if len(headcont)>0:
            scur,stotal=headcont[0].split(',')
            cur=int(scur)
            total=int(stotal)
            cur=cur+1
            if cur<total:
                headcont[0]=f'{cur},{stotal}'
                with fn.open('w') as lf:
                    lf.writelines(headcont)
                wpname=headcont[cur]
                if wpname.endswith('\n'):
                    return wpname[:-1]
                else:
                    return wpname
    return newList(path,fn,logf)
class WallpaperAwww():
    def __init__(self,wallpaper_dir,num):
        self.__dir=wallpaper_dir
        self.__log=mylog.WaybarLog('/tmp/waybar.log')
        self.__counter=counter.Counter('/tmp/wallpaper.count')
        self.__cntnum=num
    def action(self):
        val=self.__counter.valueBeforeDec()
        if val>self.__cntnum:
            wp=loadPic(self.__dir,self.__log)
            self.__log.info(f'运行awww 设置背景 {wp}')
            result = subprocess.run(['awww', 'img', '-t', 'random' ,wp], capture_output=True, text=True, check=True)
            #self.__log.info(result)
            self.__counter.setValue(self.__cntnum)
        self.__text=f'{val}'
    def atOnce(self):
        wp=loadPic(self.__dir,self.__log)
        self.__log.info(f'手动设置背景 {wp}')
        try:
            res=subprocess.run(['awww', 'img', '-t', 'random' ,wp], capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            self.__log.info(e)

    def dump(self):
        print(json.dumps({
            "text": self.__text,
            "class": "custom/wallpaper"
        }))

if __name__=='__main__':
    import sys
    try:
        cfg=loadCfg(os.environ['HOME']+'/.config/waybar/wallpaper.ini')
        num=int(cfg['count_total'])
    except ValueError:
        num=100
    except Exception as e:
        print(e)
        exit()
    
    wa=WallpaperAwww(cfg['path'],num)
    if len(sys.argv)>1:
        if sys.argv[1]=='next':
            wa.atOnce()
            exit()
        if sys.argv[1]=='test':
            exit()
            
    wa.action()
    wa.dump()
    

