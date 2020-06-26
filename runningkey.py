""" Running Key cipher, a Vigenere cipher where the key is longer than the plaintext.

More info:
https://en.wikipedia.org/wiki/Running_key_cipher
http://practicalcryptography.com/ciphers/classical-era/running-key/
"""
from vigenere import Vigenere


class RunningKey(Vigenere):
    def __init__(self, key):
        super().__init__(key)

    def encrypt(self, plaintext):
        """ Encrypt plaintext using Running Key cipher

        :param plaintext: Plaintext to encrypt
        :return: Encrypted plaintext
        """
        if len(self.key) < len(plaintext):
            raise ValueError("Key length must be longer than plaintext.")

        return self.rotate_string(plaintext)

    def decrypt(self, ciphertext):
        """ Decrypt plaintext using Running Key cipher

        :param ciphertext: Ciphertext to decrypt
        :return: Decrypted ciphertext
        """
        if len(self.key) < len(ciphertext):
            raise ValueError("Key length must be longer than plaintext.")

        return self.rotate_string(ciphertext, True)
