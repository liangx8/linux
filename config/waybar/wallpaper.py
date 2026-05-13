import os
import io
import json
import pathlib
import random
import subprocess
import mylog
import waybar_socket
import pack
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
        logf.info(f'读取目录{path}中到图片出错')
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
TOTAL_SEC = 80
class WallpaperAwww():
    def __init__(self,wallpaper_dir):
        self.__dir=wallpaper_dir
        self.__log=mylog.WaybarLog('/tmp/waybar.log')
        
    def action(self,sk):
        pi=pack.PackValueBeforeDec(1)
        out=io.BytesIO()
        pi.writeTo(out)
        sk.sendall(out.getvalue())
        bres=sk.recv(1000)
        code,val=pack.unresult(bres)
        if code==0:
            self.__text=f'{val}'
            # print(json.dumps({
            #     "text": f'{val}',
            #     "class": "custom/wallpaper"
            # }))
            if val>TOTAL_SEC:
                wp=loadPic(self.__dir,self.__log)
                self.__log.info(f'运行awww 设置背景 {wp}')
                result = subprocess.run(['awww', 'img', '-t', 'random' ,wp], capture_output=True, text=True, check=True)
                #self.__log.info(result)
                return self.resetCounter
            return None
        return self.resetCounter
    def resetCounter(self,sk):
        pi=pack.PackInt(1,TOTAL_SEC)
        out=io.BytesIO()
        pi.writeTo(out)
        sk.sendall(out.getvalue())
        bres=sk.recv(1000)
        code,val=pack.unresult(bres)
        self.__text=f'{TOTAL_SEC}'
    def onerr(self,e):
        self.__text=f'{e}'
    def atOnce(self):
        wp=loadPic(self.__dir,self.__log)
        self.__log.info(f'手动设置背景 {wp}')
        _ = subprocess.run(['awww', 'img', '-t', 'random' ,wp], capture_output=True, text=True, check=True)
        #self.__log.info(result)

    def dump(self):
        print(json.dumps({
            "text": self.__text,
            "class": "custom/wallpaper"
        }))

'''
import subprocess

# 执行 ls -l 命令
result = subprocess.run(['ls', '-l'], capture_output=True, text=True, check=True)

# 打印标准输出
print(result.stdout)

'''


def other():
    out=io.BytesIO()
    pi=pack.PackShutdown()
    pi.writeTo(out)
    print(out.getvalue())
    print(pack.unpack(out.getvalue()))

    pi=pack.PackInt(1,1)
    out.seek(0,io.SEEK_SET)
    pi.writeTo(out)
    out.truncate()
    print(out.getvalue())
    print(pack.unpack(out.getvalue()))

    pi=pack.PackStr(2,"中文")
    out.seek(0,io.SEEK_SET)
    pi.writeTo(out)
    out.truncate()
    print(out.getvalue())
    print(pack.unpack(out.getvalue()))

    pi=pack.PackGetValue(2)
    out.seek(0,io.SEEK_SET)
    pi.writeTo(out)
    out.truncate()
    print(out.getvalue())
    print(pack.unpack(out.getvalue()))

    pi=pack.PackValueBeforeGet(15)
    out.seek(0,io.SEEK_SET)
    pi.writeTo(out)
    out.truncate()
    print(out.getvalue())
    print(pack.unpack(out.getvalue()))
def action(client):
    out=io.BytesIO()

    #pi=pack.PackGetValue(20)
    #pi=pack.PackStr(2,'欢迎')
    pi=pack.PackShutdown()
    #pi=pack.PackInt(1,9)
    #pi=pack.PackValueBeforeDec(1)
    #pi=pack.PackGetValue(1)
    pi.writeTo(out)
    client.sendall(out.getvalue())
    bres=client.recv(1000)
    print(pack.unresult(bres))
def sample():
    waybar_socket.skclient(action)

if __name__=='__main__':
    #sample()
    #other()
    import sys
    wa=WallpaperAwww(os.environ['HOME']+'/wallpapers/')
    if len(sys.argv)>1:
        pass
        if sys.argv[1]=='next':
            wa.atOnce()
            exit()
    func=wa.action
    while True:
        if func == None:
            break
        else:
            func=waybar_socket.skclient(func,wa.onerr)
    wa.dump()
    

