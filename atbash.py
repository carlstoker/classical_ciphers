""" Atbash, a substitution cipher with a shift of 13

More info:
https://en.wikipedia.org/wiki/Atbash
http://practicalcryptography.com/ciphers/classical-era/atbash-cipher/
"""
from affine import Affine


class Atbash(Affine):
    def __init__(self):
        super().__init__(25, 25)