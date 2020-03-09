import binascii as ba

def b64ToHex(b64String):
    binary = ba.a2b_base64(b64String)
    convertedToHex = ba.b2a_hex(binary)
    return convertedToHex

def hexToB64(hexString):
    binary = ba.a2b_hex(hexString)
    convertedToB64 = ba.b2a_base64(binary, newline=False)
    return convertedToB64