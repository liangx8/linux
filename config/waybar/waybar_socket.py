import socket
import os
SOCKET_NAME = '/tmp/waybar-service.sock'
def skserver(callback):
    try:
        os.unlink(SOCKET_NAME)
    except OSError:
        print(f'remove {SOCKET_NAME} error')
        if os.path.exists(SOCKET_NAME):
            raise
    with socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) as sf:
        sf.bind(SOCKET_NAME)
        sf.listen(1)
        callback(sf)
def skclient(callback,ecb):
    try:
        with socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) as sf:
            sf.connect(SOCKET_NAME)
            return callback(sf)
    except Exception as e:
        ecb(e)
