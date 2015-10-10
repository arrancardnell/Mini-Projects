__author__ = 'Arran'

"""
Caesar Cipher encryption method. Encrypts a file by chosing a key at random and then incrementing each letter of the
file by the chosen key. The encrypted file and the key are then returned.
"""

import random


class CaesarCipher(object):

    def encryption(self, filename, key=None):
        """
        Encrypts the chosen file using a Caesar Cipher and provides the user with the key
        needed to decrypt the file.
        """

        if not key:
            key = random.randint(1, 25)
        encrypted = ''

        for letter in filename:
            if letter.isalpha():
                num = ord(letter)
                num += key

                if letter.isupper():
                    if num > ord('Z'):
                        num -= 26  # if the new letter is greater than "Z", cycle back round the start.
                    elif num < ord('A'):
                        num += 26  # if the new letter is less than "A", move to the end.
                elif letter.islower():
                    if num > ord('z'):
                        num -= 26  # if the new letter is greater than "z", cycle back round the start.
                    elif num < ord('a'):
                        num += 26  # if the new letter is less than "a", move to the end.

                encrypted += chr(num)
            else:
                encrypted += letter  # leaves punctuation unchanged.

        return encrypted, key