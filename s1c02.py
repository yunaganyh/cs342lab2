import s1c01
import binascii as ba

def xor(s1, s2):
    s3 = []
    for (i,j) in zip(s1,s2):
        xor = i^j
        s3.append(xor)
    return bytes(s3)
