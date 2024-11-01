string = '4854427b66307262316464336e5f6d346e753563723170375f31355f316e5f3768335f77316c647d'

chars = [f'0x{string[i:i+2]}' for i in range(0, len(string), 2)]

chars = [int(i, 16) for i in chars]

print(''.join([chr(i) for i in chars]))
