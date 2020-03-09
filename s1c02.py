import s1c01
import binascii as ba

def hexToBinary(hexString):
    return ba.a2b_hex(hexString)

def convertToBytes(string):
    return bytes(string, 'utf-8')

def xor(s1, s2):
    s3 = b''
    b1 = hexToBinary(s1)
    b2 = hexToBinary(s2)
    for (i,j) in zip(b1,b2):
        xor = convertToBytes('{0:02x}'.format(int(hex(i^j), 16)))
        s3 += xor
    return s3
