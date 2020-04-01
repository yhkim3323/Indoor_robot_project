## bluetooth code for client
import sys
sys.path.append("/usr/lib/python3/dist-packages")
import socket
import smbus
import time

host = 'B8:27:EB:D5:0C:39'
port = 1


def run_client(A):
    
    with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as s:
        s.connect((host, port))
        while 1:
            data = A
            s.sendall(data.encode())
            res = s.recv(1024)
            print(res.decode())

    '''
        for _ in range(10):
            data = input(">>")
            s.sendall(data.encode())
            if data == 'bye':
                s.close()
                break
            res = s.recv(1024)
            print(res.decode())
    '''
if __name__ == '__main__':
    run_client("3")

