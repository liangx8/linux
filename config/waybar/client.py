import socket
import pack
import io

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

def sample(sfn):
    out=io.BytesIO()
    with socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) as client:
        client.connect(sfn)
        #pi=pack.PackGetValue(20)
        #pi=pack.PackStr(2,'欢迎')
        #pi=pack.PackShutdown()
        pi=pack.PackInt(1)
        #pi=pack.PackGetValue(1)
        pi.writeTo(out)
        client.sendall(out.getvalue())
        bres=client.recv(1000)
        print(pack.unresult(bres))


if __name__=='__main__':
    sample('/tmp/waybar-service.sock')
    #other()
