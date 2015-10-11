__author__ = 'Arran'

"""
This program takes a file as an input and encrypts it using a very
simple Caesar Cipher. A file can also be decrypted if the user
knows the secret key.
"""

import random, time
from Caesar_Cipher_Encrypt import CaesarCipher
from Caesar_Decoder import CaesarDecoder


class Encrypter(object):
    """
    An encryption / decryption program.
    """
    def __init__(self):
        self.CaesarCipher = CaesarCipher()
        self.CaesarDecoder = CaesarDecoder()

    def open_file(self):
        """
        Allows user to choose a file to open.
        """

        file_name = input("\nEnter the name of the text file you would like to encrypt/decrypt." \
                     + "\nPlease include the suffix (i.e. '.txt')." + "\n> ")

        try:
            with open(file_name, "r") as f:
                file_contents = f.read()
            return file_contents.strip("\n")
        except IOError as ioerr:
            print("\nFile error: " + str(ioerr))
            return self.open_file()

    def encrypt_or_decrypt_file(self):
        """ 
        Open a file and then allow users to encrypt or decrypt it.
        """

        file = self.open_file()
        choice = input("\nDo you want to [e]ncrypt or [d]ecrypt the file?"
                       + "\n> ").lower()

        if choice[0] == "e":
            cipher_file, cipher_key = self.CaesarCipher.encryption(file)
            print(cipher_file)
            print("\nYour key is {}. Please remember this to decode your message.\n".format(cipher_key))
        elif choice[0] == "d":

            decode = input("Do you know the decryption key?\n> ").lower()

            if decode in "yes":
                try:
                    cipher_key = int(input("\nPlease enter the key (whole number) to decode your file.\n> "))
                except ValueError as valerr:
                    print("Value error: " + str(valerr))

                cipher_key = -cipher_key
                cipher_file, cipher_key = self.CaesarCipher.encryption(file, cipher_key)
                print("\nUsing the key {}, your decoded message is:\n".format(-cipher_key))
                print(cipher_file)
            else:
                print("Attempting to decrypt the file...")
                time.sleep(1)
                print("Attempting to decrypt the file...")
                time.sleep(1)
                cipher_file, cipher_key = self.CaesarDecoder.decrypter(file)
                print("\nUsing the key {}, your decoded message is:\n".format(-cipher_key))
                print(cipher_file)

        save = input("\nWould you like to save the file?" + "\n> ").lower()

        if save in "yes":
            save_file_name = input("Please choose a name for the file." + "\n> ").lower()
            self.save_file(save_file_name, cipher_file)

    def save_file(self, filename, text):
        """
        Saves the encrypted / decrypted text to a file if requested.
        """

        with open(filename + ".txt", "w") as f:
            f.write(text)

if __name__ == "__main__":
    encrypt = Encrypter()
    encrypt.encrypt_or_decrypt_file()