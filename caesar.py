""" Caesar cipher, a substitution cipher with a shift of 3

More info:
https://en.wikipedia.org/wiki/Caesar_cipher
http://practicalcryptography.com/ciphers/classical-era/caesar/
"""
from substitution import Substitution


class Caesar(Substitution):
    def __init__(self):
        super().__init__(3)