# Encoded flag decoded from base64 2 times
halfway = "wpjvJAM{jhlzhy_k3jy9wa3k_m0212758}"

flag = ""

cap = {i - 64:chr(i) for i in range(65,91)}
low = {i - 96:chr(i) for i in range(97,123)}

for char in halfway:
    if char not in cap.values() and char not in low.values():
        flag += char
    if char in low.values():
        position = ord(char) - 96
        flag += chr(((position + 19) % 26) + 96)
    if char in cap.values():
        position = ord(char) - 64
        flag += chr(((position + 19) % 26) + 64)
    
print(flag)
