encrypted = 'DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL'


def fromIdentityMap(x):
    return x - 0x75

def toIdentityMap(x):
    return chr(x + 0x41)

def decrypt(encrypted):
    flag = ''
    for i in range(len(encrypted)):
        char = encrypted[i]
        if not char.isalpha():
            flag += char
        else:
            chi = fromIdentityMap(ord(char) - i)
            ch = toIdentityMap(chi % 26)
            flag += ch
    return flag

print('HTB{' + decrypt(encrypted) + '}')
