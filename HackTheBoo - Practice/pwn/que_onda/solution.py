from pwn import *

context.log_level = 'critical'

address = '83.136.252.65'
port = 30553

with remote(address,port) as target:
	target.recvuntil(b'$ ')
	target.sendline(b'flag')
	print(target.recvuntil(b'}').decode().strip())
