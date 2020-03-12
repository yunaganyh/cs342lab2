from s1c02 import xor
from s1c03 import createElongatedKey

def vigenereEncrypt(message, key):
    cipher = []
    key = createElongatedKey(key, len(message))
    for (i,j) in zip(message, key):
        encrypt = i^j
        cipher.append(encrypt)
    return bytes(cipher)


def vigenereDecrypt(cipher, key):
    message = []
    key = createElongatedKey(key, len(cipher))
    for (i,j) in zip(cipher, key):
        decrypt = i^j
        message.append(decrypt)
    return bytes(message)
