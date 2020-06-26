""" ROT13 Cipher, a substitution cipher with a shift of 13

More info:
https://en.wikipedia.org/wiki/ROT13
http://practicalcryptography.com/ciphers/classical-era/rot13/
"""
from substitution import Substitution


class Rot13(Substitution):
    def __init__(self):
        super().__init__(13)