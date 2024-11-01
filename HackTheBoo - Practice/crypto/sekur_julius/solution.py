encrypted = open('output.txt', 'r').read().strip()

decrypted = [chr((((ord(i)) - 2) % 26) + 65) if ord(i) in range(65,91) else i for i in encrypted]

print(''.join(decrypted).replace('0', ' '))
