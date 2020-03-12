import codecs, sys

def binary(s):
    return bytes(bin(int(s, 16))[2:], 'utf-8')

def editDistance(s1, s2):
    count = 0
    s1 = binary(codecs.encode(s1, "hex"))
    s2 = binary(codecs.encode(s2, "hex"))
    for (i,j) in zip(s1, s2):
        if i^j == 1:
            count += 1
    return count

def findKeysize(cipher, maxKeysize):
    keysizes = [i for i in range(2, maxKeysize)]
    smallestEditDist = sys.maxsize
    keyLen = 0
    for i in keysizes:
        s1 = cipher[0:i]
        s2 = cipher[1:i+1]
        dist = editDistance(s1, s2)/i
        if dist < smallestEditDist:
            smallestEditDist = dist
            keyLen = i
    return keyLen

def solveS1C06(cipher):
    keySize = findKeysize(cipher, 40)
    