__author__ = 'Arran'

"""
This program can be used to decode an encrypted file created by the Caesar Cipher. The decoder will cycle through all
the possible keys and will determine which key generates a file containing the most English words. It will then return
the decrypted file.
"""

from Caesar_Cipher_Encrypt import CaesarCipher


class CaesarDecoder(object):
    """
    Decode a Caesar Cipher when the key is not known.
    """

    def __init__(self):
        """
        Setup the Caesar Cipher to cycle through the keys and create a list of all english words.
        """

        self.CaesarCipher = CaesarCipher()
        self.words_list = self.open_file()

    def open_file(self):
        """
        Open the dictionary of English words to compare the decrypted words against.
        """

        try:
            with open("english_words.txt", "r") as f:
                file_contents = f.read()
            return file_contents.strip("\n")
        except IOError as ioerr:
            print("\nFile error: " + str(ioerr))
            return self.open_file()

    def decrypter(self, file):
        """
        Cycle through all the possible keys of the Caesar Cipher, decrypt the file using each key and compare the
        decrypted words to words in the English dictionary file. The key with the most recognised English words will be
        the one returned.
        """

        key = 0
        total_decoded_words = 0
        best_decoded_file = None

        for x in range(1,26):

            decoded_words = 0
            cipher_key = -x
            decoded_file, cipher_key = self.CaesarCipher.encryption(file, cipher_key)

            for word in decoded_file.split():
                if word in self.words_list:
                    decoded_words += 1

            if decoded_words > total_decoded_words:  # if there are more decoded words than the previous key, update key
                total_decoded_words = decoded_words
                key = cipher_key
                best_decoded_file = decoded_file

        return best_decoded_file, key