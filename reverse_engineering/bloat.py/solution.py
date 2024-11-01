import os

a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

password = a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]

print(f'Password: {password}')

with open('password.txt', 'w') as passwordFile:
	passwordFile.write(password)

os.system(f'python3 bloat.flag.py < password.txt')

