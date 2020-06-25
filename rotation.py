def rotate_char(char, shift):
    """ Rotate a character by the value of shift, mod 26

    :param char: Character to rotate
    :param shift: Number of characters to rotate
    :return:
    """
    # Determine whether the character is alphabetic. If it is, set an
    # appropriate offset. If not, return the character.
    if 65 <= ord(char) <= 90:
        ascii_offset = 65
    elif 97 <= ord(char) <= 122:
        ascii_offset = 97
    else:
        return char

    # Calculate the new character's codepoint using char's index within the
    # alphabet, adding the shift, getting the mod 26 value of that, then
    # adding the ASCII offset back.
    new_codepoint = (ord(char) - ascii_offset + shift) % 26 + ascii_offset

    return chr(new_codepoint)


def rotate_string(string, shift):
    """ Rotate each character in the string.

    :param string: String to rotate
    :param shift: Amount to shift each character
    :return: Rotated string
    """
    return "".join(rotate_char(c, shift) for c in string)


class Rotate:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, plaintext):
        """ Encrypt plaintext

        :param plaintext: Plaintext to encrypt
        :return: Encrypted plaintext
        """
        return rotate_string(plaintext, self.shift)

    def decrypt(self, ciphertext):
        """ Decrypt ciphertext

        :param ciphertext: Ciphertext to decrypt
        :return: Decrypted ciphertext
        """
        return rotate_string(ciphertext, self.shift * -1)
