'''
From this point on, I'm not providing the number of arguments.
Part of your job is to understand the contracts of these methods
and how they fit together.
'''
import s1c02
import binascii as ba

def createElongatedKey(key, length):
    return key*(length // len(key) + 1)

def caesarEncrypt(message, key):
    elongatedKey = createElongatedKey(key, len(message))
    return s1c02.xor(message, elongatedKey)

'''
can decrypt and get original message as long as you have one part
of the original xor pair.
'''
def caesarDecrypt(cipher, key):
    elongatedKey = createElongatedKey(key, len(cipher))
    return s1c02.xor(cipher, elongatedKey)

def bytesToHex(byteString):
    return bytes.hex(byteString)


#decrypted string is in raw bytes
def scoreText(decryptedString):
    #E A R I O T N S L C
    mostCommon = ['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c']
    mostCommon.extend([i.capitalize() for i in mostCommon])
    mostCommon = [hex(ord(i)) for i in mostCommon]
    #B F Y W K V X Z J Q
    leastCommon = ['b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q']
    leastCommon.extend([i.capitalize() for i in leastCommon])
    leastCommon = [hex(ord(i)) for i in leastCommon]
    
    decryptedList = [hex(i) for i in list(decryptedString)]

    score = 0

    for i in decryptedList:
        if i in mostCommon:
            score += 30
        elif i in leastCommon:
            score -= 5
        elif (int(i,16) < 0x20 or int(i,16) >= 0x7F):
            score -= 100
        else:
            score += 10
    return score


def binToHex(binary):
        return ba.b2a_hex(binary)

def hexToBin(hexString):
    return ba.a2b_hex(hexString)

def solveS1C03(cipher):
    keys = [bytes(hex(i)[2:].zfill(2), 'utf-8') for i in range(256)]
    decrypts = [caesarDecrypt(cipher,hexToBin(ki)) for ki in keys]
    scores = [scoreText(decr) for decr in decrypts]
    highest = (decrypts[scores.index(max(scores))], max(scores))
    return highest
