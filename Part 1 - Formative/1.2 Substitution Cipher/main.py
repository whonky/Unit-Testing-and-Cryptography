# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    """

    :param text: The text to be encoded
    :param codebet: The scrambled alphabet
    :return encoded_word: The encoded word
    """
    encoded_word = ""
    for letter in text:
        index = alpha.index(letter)
        encoded_word += codebet[index]
    return encoded_word


def sub_decode(text, codebet):
    """

    :param text:
    :param codebet:
    :return:
    """
    decoded_word = ""
    for letter in text:
        index = alpha.index(letter)
        encoded_word += codebet[index]
    return ""


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
