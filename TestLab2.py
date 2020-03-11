import unittest

from s1c01 import b64ToHex, hexToB64
from s1c02 import xor, hexToBinary
from s1c03 import solveS1C03, caesarEncrypt, caesarDecrypt, scoreText
from s1c04 import solveS1C04
from s1c05 import vigenereEncrypt, vigenereDecrypt
from s1c06 import editDistance, solveS1C06
from s1c07 import AES_ECB_encrypt, AES_ECB_decrypt
from s1c08 import solveS1C08

class TestLab2(unittest.TestCase):

    '''Here's an example of what some test cases might look like.'''
    # @unittest.skip('Not yet implemented')
    def test_s1c01_hexToB64(self):
        testCases = [
            (
                b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
                b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
            ),
            (b'4e6f6e204d696e6973747261726920736564204d696e69737472617265', b'Tm9uIE1pbmlzdHJhcmkgc2VkIE1pbmlzdHJhcmU='),
            (b'', b''),
            (b'61', b'YQ=='),
            (b'6666666664643435', b'ZmZmZmRkNDU=')

        ]
        for hexString, b64String in testCases:
            self.assertEqual(hexToB64(hexString), b64String)
            self.assertEqual(type(hexToB64(hexString)), bytes)

    '''One more example.'''

    def test_s1c01_b64ToHex(self):
        testCases = [
            (
                b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
                b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
            ),
            (b'4e6f6e204d696e6973747261726920736564204d696e69737472617265', b'Tm9uIE1pbmlzdHJhcmkgc2VkIE1pbmlzdHJhcmU='),
            (b'', b''),
            (b'61', b'YQ=='),
            (b'6666666664643435', b'ZmZmZmRkNDU=')

        ]
        for hexString, b64String in testCases:
            self.assertEqual(b64ToHex(b64String), hexString)

    # @unittest.skip('Not yet implemented')
    def test_s1c02_xor(self):
        '''
        Starting here, write your own tests. You can generate tests in a variety
        of ways, ranging from trivial tests (does the empty string produce the empty
        string?) to tests of properties (does xor preserve length?) to tests of types
        (is the return type of this method correct?) to specific cases (is the xor
        of these two specific byte strings equal to the correct byte string?).

        To generate specific cases, I'd suggest either using very small examples 
        you can work by hand, or generate the test cases using other code you write
        or online calculators.
        '''
        testCases = [
            (b'1c0111001f010100061a024b53535009181c', 
             b'686974207468652062756c6c277320657965',
             b'746865206b696420646f6e277420706c6179'
            ),
            (b'',b'',b''),
            (b'1234', b'5678', b'444c')
        ]
        for hexString1, hexString2, result in testCases:
            xorred = xor(hexToBinary(hexString1), hexToBinary(hexString2))
            self.assertEqual(xorred, hexToBinary(result))
            self.assertEqual(type(xorred), bytes)

    # @unittest.skip('Not yet implemented')
    def test_s1c03_caesarEncrypt(self):
        testCases = [
        (b'0123456789ABCDEF',
         b'c3e187a54b690f2d',
         b'C2'
        ),
        (b'0123456789ABCDEF',
         b'5c7e183ad4f690b2',
         b'5D'
        ),
        (b'',b'',b'AF')
        ]
        for hexString, cipher, key in testCases:
            hexString = hexToBinary(hexString)
            cipher = hexToBinary(cipher)
            key = hexToBinary(key)
            encrypted = caesarEncrypt(hexString, key)
            self.assertEqual(encrypted, cipher)
            self.assertEqual(type(encrypted), bytes)
            self.assertEqual(len(hexString), len(cipher))
            #test that can encrypt with all possible hex bytes
            for i in range(0xff):
                k = bytes('{:02x}'.format(i), 'utf-8')
                encrypted = caesarEncrypt(hexString, k)


    # @unittest.skip('Not yet implemented')
    def test_s1c03_caesarDecrypt(self):
        testCases = [
        (b'c3e187a54b690f2d',
         b'0123456789abcdef',
         b'C2'
        ),
        (b'5c7e183ad4f690b2',
         b'0123456789abcdef',
         b'5D'
        ),
        (b'',b'',b'AF')
        ]
        for cipher, message, key in testCases:
            message = hexToBinary(message)
            cipher = hexToBinary(cipher)
            key = hexToBinary(key)
            decrypted = caesarDecrypt(cipher, key)
            self.assertEqual(decrypted, message)
            self.assertEqual(type(decrypted), bytes)
            self.assertEqual(len(message), len(decrypted))
            #test that can decrypt with all possible hex bytes
            for i in range(0xff):
                k = bytes('{:02x}'.format(i), 'utf-8')
                decrypted = caesarDecrypt(cipher, k)

    # @unittest.skip('Not yet implemented')
    def test_s1c03_scoreText(self):
        testCases = [
        (b'hello world', 33),
        (b'call me ishmael', 55),
        (b'!!!!!!!!!!!!!!!', 15)
        ]
        for string, res in testCases:
            score = scoreText(string)
            self.assertEqual(type(score), int)
            # self.assertEqual(score, res)


    '''
       ********
       Remember! You can and should add more test methods to this file to test 
       other helper methods that you write in the course of this lab.
       ********
    '''


    # @unittest.skip('Not yet implemented')
    def test_s1c03_solveS1C3(self):
        '''
        You might find that it's less clear what the testable contract of the methods
        that just solve the challenges is. If you choose, you can decide not to use
        this test method, and instead just test the helper methods you write to make
        solveSXCY() methods work.
        '''
        testCases = [
        (b'hello world!', b'C4'),
        (b'It was a bright cold day in April, and the clocks were striking thirteen.', b'55'),
        (b'It"s no use going back to yesterday, because I was a different person then.', b'a2'),
        (b'Who in the world am I?!?!?! Ah, that"s the great puzzle! :D', b'07'),
        (b'"She said that the homework #123#345#456S --- IDK WHAT --- is due on monday!!!":::::', b'73')
        ]
        for hexString, key in testCases:
            key = hexToBinary(key)
            encrypted = caesarEncrypt(hexString, key)
            self.assertEqual(type(encrypted), bytes)
            decryption = solveS1C03(encrypted)[0]
            self.assertEqual(decryption, hexString)

    # @unittest.skip('Not yet implemented')
    def test_s1c04_solveS1C4(self):
        print(solveS1C04("4.txt"))

    @unittest.skip('Not yet implemented')
    def test_s1c05_vigenereEncrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c05_vigenereDecrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c06_editDistance(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c06_solveS1C6(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c07_AES_ECB_encrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c07_AES_ECB_decrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c08_solveS1C8(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
