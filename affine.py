class Affine:
    def __init__(self, key_a, key_b, alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.key_a = key_a
        self.key_b = key_b
        self.alphabet = alphabet

    def encrypt(self, plaintext):
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


# Create Affine algorithm using 9 and 4 as the keys, using the default lowercase
# alphabet.
affine = Affine(25, 25)
print(affine.encrypt("abcdefg"))
