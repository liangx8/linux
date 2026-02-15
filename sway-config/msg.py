import os
import socket
import io
cmd='output * bg /home/com/wallpaper/beauty1.png fit'
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
            print(data.decode())
        
    
if __name__ == '__main__':
    
    demo(os.environ['SWAYSOCK'])
