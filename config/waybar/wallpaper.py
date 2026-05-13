import io
import json
import waybar_socket
import pack

class WallpaperAwww():
    def __init__(self,wallpaper_dir):
        self.__dir=wallpaper_dir
        
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
            if val>50:
                return self.action1
            return None
        return self.action1
    def action1(self,sk):
        pi=pack.PackInt(1,50)
        out=io.BytesIO()
        pi.writeTo(out)
        sk.sendall(out.getvalue())
        bres=sk.recv(1000)
        code,val=pack.unresult(bres)
        self.__text="50"
    def onerr(self,e):
        self.__text=f'{e}'
    def dump(self):
        print(json.dumps({
            "text": self.__text,
            "class": "custom/wallpaper"
        }))


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
    wa=WallpaperAwww('')
    func=wa.action
    while True:
        if func == None:
            break
        else:
            func=waybar_socket.skclient(func,wa.onerr)
    wa.dump()

    

