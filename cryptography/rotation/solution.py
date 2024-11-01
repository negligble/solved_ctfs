encrypted = 'xqkwKBN{z0bib1wv_l3kzgxb3l_25l7k61j}'

flag = ''

for char in encrypted:
    if not char.isalpha():
        flag += char
    elif char.islower():
        flag += chr((ord(char) + 25) % 26 + 97)
    else:
        flag += chr((ord(char) + 5) % 26 + 65)

        
print(flag)