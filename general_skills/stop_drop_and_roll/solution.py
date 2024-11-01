import socket
import time
import re

def receiveIntro(target):
    target.settimeout(2)
    intro = b''
    while True:
        try:
            intro += target.recv(1024)
        except Exception:
            return 

def challengeResponse(target):
    target.settimeout(3)
    values = {'GORGE':'STOP',
              'PHREAK':'DROP',
              'FIRE':'ROLL'}
    
    while True:
        try:
            data = ''
            while ('GORGE' not in data and 'PHREAK' not in data and 'FIRE' not in data and 'HTB{' not in data):
                data = target.recv(1024).decode()
                if 'Unfortunate! You died!' in data:
                    break
            if 'HTB{' in data:
                return data
            pattern = r'\b(?:' + '|'.join(values.keys()) + r')\b'
            challengeCodes = re.findall(pattern, data)
            responseCodes = '-'.join([values[key] for key in challengeCodes])
            target.send((responseCodes + '\n').encode())
        except Exception as e:
            print(f'{e} occured.')
            break
    
    
address = '94.237.61.218'
port = 48029

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address,port))

with s as target:
    receiveIntro(target)
    target.send('y\n'.encode())
    print(challengeResponse(target))
