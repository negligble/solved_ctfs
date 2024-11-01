from pwn import *
from Crypto.PublicKey import RSA
from sage.all import *
import warnings

warnings.filterwarnings('ignore')

context.log_level = 'critical'

address = '94.237.62.14'
port = 34957

with remote(address,port) as target:
	for i in range(5):
		target.recvuntil('🎃Can you crack this pumpkin🎃?\n')

		rsaKey = target.recvuntil(b'-----END PUBLIC KEY-----\n')

		rsaKey = RSA.importKey(rsaKey)

		print(f'Cracking {i+1}')

		n = rsaKey.n
		e = rsaKey.e

		p, q = factor(n)

		target.recvuntil(b'enter your first pumpkin = ')
		target.sendline(str(p[0]))
		target.recvuntil(b'enter your second pumpkin = ') 
		target.sendline(str(q[0]))
		print(f'Cracked {i+1}')
		target.recvline()

	flag = target.recvline().decode()
	print(f'Flag: {flag}')
