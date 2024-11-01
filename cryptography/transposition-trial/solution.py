encryptedFlag = [char for char in 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7']

for i in range(2, len(encryptedFlag) - 3, 3):
    encryptedFlag[i] = encryptedFlag[i + 3]
        
print(f'T{"".join(encryptedFlag[:-1])}')
  

    
