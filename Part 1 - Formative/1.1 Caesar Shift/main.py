# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    """
    Encodes a word with a Caesar Cipher of a given shift.
    :param text: The text to be encoded.
    :param n: The number of letters to shift to the right.
    :return encoded_word: The encoded text.
    """
    encoded_word = ""
    for letter in text:
        index = alpha.index(letter.upper())
        index = (index + n) % 26
        encoded_word += alpha[index]
    return encoded_word


def caesar_decode(text, n):
    """
    Decodes a word coded with the Caesar Cipher of a given shift.
    :param text: The text to be decoded.
    :param n: The number of letters to shift to the left.
    :return decoded_word: The decoded text.
    """
    decoded_word = ""
    for letter in text:
        index = alpha.index(letter.upper())
        print(index)
        decoded_word += alpha[index - n]
    return decoded_word


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
