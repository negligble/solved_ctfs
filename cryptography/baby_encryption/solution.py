print(''.join([chr((i - 18) * pow(123, -1, 256) % 256 ) for i in [i for i in bytes.fromhex(open('msg.enc', 'r').read())]]))
