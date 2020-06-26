""" Gronsfeld cipher, a Vigenere cipher using numbers instead of letters.

More info:
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Variants
http://practicalcryptography.com/ciphers/classical-era/vigenere-gronsfeld-and-autokey/
"""
from vigenere import Vigenere
import string


class Gronsfeld(Vigenere):
    def __init__(self, key, alphabet=string.ascii_lowercase):
        self.key = key
        self.alphabet = alphabet

        chars = "".join(alphabet[i] for i in key)
        super().__init__(chars, alphabet)
