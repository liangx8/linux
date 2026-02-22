import os
import socket
import io
import json
cmd='output * bg /home/com/wallpaper/beauty1aa.png fit'
def demo(sock):
    with socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) as sf:
        sf.connect(sock)
        print(f"connect {sock} successful")
        with io.BytesIO() as buf:
            buf.write('i3-ipc'.encode())
            cmdbuf=cmd.encode()
            buf.write(len(cmdbuf).to_bytes(4,'little'))
            buf.write(bytes((0,0,0,0)))
            buf.write(cmdbuf)
            sf.sendall(buf.getvalue())
            data=sf.recv(1000)
            cnt=int.from_bytes( data[6:10],'little')
            ty=int.from_bytes(data[10:14],'little')
            buf=json.loads(data[14:])
            print(buf,type(buf[0]),cnt,ty)
            
        
    
if __name__ == '__main__':
    
    demo(os.environ['SWAYSOCK'])
