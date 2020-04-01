import socket
import time

def run_server(host='B8:27:EB:D5:0C:39',port = 1):
    buf_size = 1024
    with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as s:
        s.bind((host,port))
        s.listen()
        conn, addr = s.accept()
        while 1:
            data = conn.recv(buf_size)
            
            msg = data.decode()
            print(data.decode())
            conn.sendall(data)
            if msg =='bye':
                conn.close()
                break
            
        

if __name__ == '__main__':
    run_server()

