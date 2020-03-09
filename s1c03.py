'''
From this point on, I'm not providing the number of arguments.
Part of your job is to understand the contracts of these methods
and how they fit together.
'''
import s1c02

def createElongatedKey(key, length):
    elongatedKey = b''
    for i in range(length//2):
        elongatedKey += key
    return elongatedKey

def caesarEncrypt(message, key):
    result = b''
    elongatedKey = createElongatedKey(key, len(message))
    return s1c02.xor(message, elongatedKey)
'''
can decrypt and get original message as long as you have one part
of the original xor pair.
'''

def caesarDecrypt(cipher, key):
    result = b''
    elongatedKey = createElongatedKey(key, len(cipher))
    return s1c02.xor(cipher, elongatedKey)


def scoreText(decryptedString):
    # mostCommon = []
    # leastCommon = []
    # specialChars = [b'21', b'22', b'23', b'24', b'25', b'26', 
    #                 b'27', b'28', b'29', b'2a', b'2b', b'2c', b'2d']
    pass

def solveS1C03():
    pass
