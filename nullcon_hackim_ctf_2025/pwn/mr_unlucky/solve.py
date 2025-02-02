from pwn import *
import time
from ctypes import CDLL

context.binary = binary = ELF('./mr_unlucky', checksec=False)
libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')

#p = process()
p = remote('52.59.124.14', 5021)

heroes = [
    'Anti-Mage',
    'Axe',
    'Bane',
    'Bloodseeker',
    'Crystal Maiden',
    'Drow Ranger',
    'Earthshaker',
    'Juggernaut',
    'Mirana',
    'Morphling',
    'Phantom Assassin',
    'Pudge',
    'Shadow Fiend',
    'Sniper',
    'Storm Spirit',
    'Sven',
    'Tiny',
    'Vengeful Spirit',
    'Windranger',
    'Zeus'
]

seed = libc.time(0x0)
libc.srand(seed)

for _ in range(0x32):
    hero_index = libc.rand() % 0x14
    correct_hero = heroes[hero_index]

    info(f'Guessing: {correct_hero}')

    p.recvuntil(b'Guess the Dota 2 hero (case sensitive!!!): ')
    p.sendline(correct_hero.encode())

    response = p.recvline().decode()
    if 'Wrong guess' in response:
        break

p.interactive()
