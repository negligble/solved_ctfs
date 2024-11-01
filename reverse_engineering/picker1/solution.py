import socket

address = 'saturn.picoctf.net'
port = 53259
payload = 'win\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address, port))

s.recv(1024)
s.send(payload.encode())

chars = s.recv(1024).decode().split(' ')[:40]
flag = ''.join([chr(int(char, 16)) for char in chars])

print(f'THE FLAG IS {flag}!!!!')