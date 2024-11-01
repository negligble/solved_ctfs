from random import choices

def julius_encrypt(msg, shift):
    ct = ''
    for p in msg:
        if p == ' ':
            ct += '0'
        elif not ord('A') <= ord(p) <= ord('Z'):
            ct += p
        else:
            o = ord(p) - 65
            ct += chr(65 + (o + shift) % 26)
    return ct

def encrypt(msg, key):
    for shift in key:
        msg = julius_encrypt(msg, shift)
    return msg

msg = open('secret.txt').read().upper()
secure_key = os.urandom(1337)

with open('output.txt', 'w') as f:
    f.write(encrypt(msg, secure_key))
