import other
import pathlib
import random
import os
import json
import socket
import io
def setbg(fn,sock):
    with socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) as sf:
        sf.connect(sock)
        with io.BytesIO() as buf:
            buf.write('i3-ipc'.encode())
            cmd=f"output * bg {fn} fill"
            cmdbuf=cmd.encode()
            buf.write(len(cmdbuf).to_bytes(4,'little'))
            buf.write(bytes((0,0,0,0)))
            buf.write(cmdbuf)
            sf.sendall(buf.getvalue())
        bres=sf.recv(1000)
        #size=int.from_bytes(bres[6:10])
        res=json.loads(bres[14:])
        if res[0]['success']:
            return None
        else:
            return res[0]

def listFiles(path):
    cb = lambda x:path+x.name
    pn=pathlib.Path(path)
    if pn.exists():
        return [cb(x) for x in pn.iterdir() if x.name.endswith('.png') or x.name.endswith('.jpg')]
    else:
        return None
def newList(path,fn,logf):
    contents=listFiles(path)
    if contents==None:
        print(f'{path} is not available',file=logf)
        return None
    print('NEW LIST',file=logf)
    random.shuffle(contents)
    cnt=len(contents)
    headcont=[f"1,{cnt}"]+contents
    with fn.open('w') as lf:
        for x in headcont:
            lf.write(x)
            lf.write('\n')
    return contents[0]

def updatePics(path,logf):
    
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
                headcont[0]=f"{cur},{stotal}"
                with fn.open('w') as lf:
                    lf.writelines(headcont)
                res=headcont[cur]
                if res.endswith('\n'):
                    return res[:-1]
                else:
                    return res
    return newList(path,fn,logf)
    
    

    
class Wallpaper(dict):
    def __init__(self,dirpath,log):
        self['background']='#1255d0'
        self.__dir=dirpath
        self.__cnt=3
        self.__log=log
        self.__sway_sock=os.environ['SWAYSOCK']
        fn=updatePics(dirpath,log)
        if fn != None:
            res=setbg(fn,self.__sway_sock)
            if res==None:
                print(f"最新背景{fn}",file=self.__log)
            else:
                print(f"尝试设置背景'{fn}'错误:\n{res}",file=self.__log)
    def onclick(self,ev):
        print(ev,file=self.__log)
        
    def update(self):
        cnt=self.__cnt
        if cnt==0 :
            self.__cnt=30
            val=updatePics(self.__dir,self.__log)
            if val==None:
                print("未知错误",file=self.__log)
                return
            res=setbg(val,self.__sway_sock)
            if res==None:
                print(f"最新背景{val}",file=self.__log)
            else:
                print(f"尝试设置背景'{val}'错误:\n{res}",file=self.__log)
        else:
            self.__cnt=cnt-1
        other.fill(self,"{:02d}".format(cnt),None,None)
