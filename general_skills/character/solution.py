import socket
import time

address = '94.237.56.229'
port =  32468

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

flag = ''

with s as target:
    target.connect((address, port))
    time.sleep(1)
    target.settimeout(2)
    target.recv(1024)
    for i in range(10000):
        try:
            print(flag)
            ch = str(i)
            target.send((ch + '\n').encode())
            response = target.recv(1024).decode()
            char = response[response.index(':') + 2]
            if char == '}':
                flag += char
                print(flag)
                break
            flag += char
        except Exception:
            print(flag)


        
        
    
    