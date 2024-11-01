encryptedFlag = 'rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}'
key = 'CYLAB'

while len(key) < len (encryptedFlag):
    key += key
    
key = key[:len(encryptedFlag)]

alphabets = []
j = 0

for i in range(26):
    alphabets.append([chr((j % 26) + 65) for j in range(j, j + 26)])
    j += 1


keyIndex = 0
flag = ''

for char in encryptedFlag:
    if not char.isalpha():
        flag += char
    elif char.islower():
        flag += alphabets[0][alphabets[alphabets[0].index(key[keyIndex])].index(char.upper())].lower()
        keyIndex += 1
    elif char.isupper():
        flag += alphabets[0][alphabets[alphabets[0].index(key[keyIndex])].index(char)]
        keyIndex += 1

print(flag)