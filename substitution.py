""" Simple Substitution cipher, which is a Vigenere cipher whose key is one letter.

More info:
https://en.wikipedia.org/wiki/Caesar_cipher
http://practicalcryptography.com/ciphers/classical-era/caesar/
"""
from vigenere import Vigenere
import string


class Substitution(Vigenere):
    def __init__(self, shift):
        alphabet = string.ascii_lowercase
        super().__init__(alphabet[shift % len(alphabet)])
