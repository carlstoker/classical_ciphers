""" Affine Cipher, another monoalphabetic substitution cipher

More info:
https://en.wikipedia.org/wiki/Affine_cipher
http://practicalcryptography.com/ciphers/classical-era/affine/
"""


class Affine:
    def __init__(self, key_a, key_b, alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.key_a = key_a
        self.key_b = key_b
        self.alphabet = alphabet
        self.modular_inverse = self.calculate_modular_inverse()

    def encrypt(self, plaintext):
        """ Encrypt plaintext using the Affine cipher

        :param plaintext: Plaintext to encrypt
        :return: Encrypted plaintext
        """
        if not is_coprime(self.key_a, len(self.alphabet)):
            return None

        ciphertext = ""

        for char in plaintext:
            # Ignore characters not in the alphabet
            if char not in self.alphabet:
                ciphertext += char
                continue

            # Calculate the new character position using the Affine algorithm.
            cipher_pos = ((self.key_a * self.alphabet.index(char)) + self.key_b)
            cipher_pos %= len(self.alphabet)

            # Add the character at that new position to the ciphertext.
            ciphertext += self.alphabet[cipher_pos]

        return ciphertext

    def decrypt(self, ciphertext):
        """ Decrypt ciphertext

        :param ciphertext: Ciphertext to decrypt
        :return: Decrypted ciphertext
        """
        if not is_coprime(self.key_a, len(self.alphabet)):
            return None

        # Initialize blank plaintext string.
        plaintext = ""

        for char in ciphertext:
            # Ignore characters not in the alphabet
            if char not in self.alphabet:
                plaintext += char
                continue

            # Calculate the new character position using the Affine algorithm.
            char_pos = self.modular_inverse * (self.alphabet.index(char) - self.key_b) % len(self.alphabet)

            # Add the character at that new position to the ciphertext.
            plaintext += self.alphabet[char_pos]

        return plaintext

    def calculate_modular_inverse(self):
        """ Find the modular inverse of key_a
        :return: Modular inverse of key_a
        """

        # Only loop through integers up to the value of the modulus.
        for x in range(len(self.alphabet)):
            # Test if the value x is the modular inverse of that number.
            if (self.key_a * x) % len(self.alphabet) == 1:
                return x

        # Otherwise, return None
        return None


def is_coprime(num1, num2):
    """ Determine if two integers are coprime using Euclid's algorithm

    :param num1: First integer
    :param num2: Second integer
    :return: Boolean of the two integers' coprime status
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1

    return max(num1, num2) == 1
