def gen(g, x, p):
    return pow(g, x) % p




def breakEncrypt(cipher, key):
    cipherTxt = ""
    for character in cipher:
        cipherTxt += (chr(int(character / (key * 311))))
    return cipherTxt




def reverseXOR(semi):
    decrypted = ""
    encKey = "trudeau"
    for i, char in enumerate(semi):
        key_char = encKey[i % len(encKey)]
        decryptedChar = chr(ord(char) ^ ord(key_char))
        decrypted += decryptedChar
    return decrypted[::-1]





def reverse_ecrypt():
    a = 95
    b = 21

    p = 97
    g = 31

    u = gen(g, a, p)
    v = gen(g, b, p)

    key = gen(v, a, p)
    sKey = gen(u, b, p)
    shared = None

    if key == sKey:
        shared = key
    else:
        print("Bad key.")
        return 
    
    cipher = [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]
    
    semi = breakEncrypt(cipher, key)
    print(reverseXOR(semi))


reverse_ecrypt()

    
