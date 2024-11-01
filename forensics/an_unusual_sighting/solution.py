from pwn import *

context.log_level = 'critical'

address = '94.237.58.171'
port = 56366


lines = [b'100.107.36.130:2221',
	b'2024-02-13 11:29:50',
	b'2024-02-19 04:00:14',
	b'OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4',
	b'whoami',
	b'./setup']

with remote(address, port) as target:
	for line in lines:
		target.recvuntil(b'>')
		target.sendline(line)

	flag = target.recvuntil(b'}').decode()
	flag = flag[flag.index('HTB'):]
	print(flag)
