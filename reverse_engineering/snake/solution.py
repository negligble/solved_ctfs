
inputList = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 105, 114, 91, 0, 71, 106, 124, 93, 78]

xorKey = 'J'
xorKey = '_' + xorKey
xorKey = xorKey + 'o'
xorKey = xorKey + '3'
xorKey = 't' + xorKey

keyList =  [ord(char) for char in xorKey]

while len(keyList) < len(inputList):
    keyList.extend(keyList)
    print(keyList)

print(''.join(chr(a^b) for a,b in zip (inputList, keyList)))
