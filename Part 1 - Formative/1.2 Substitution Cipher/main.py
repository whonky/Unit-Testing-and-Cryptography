# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    """
    Encodes a word with a substitution cipher.
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
    Decodes a word coded with a substitution cipher.
    :param text: The text to be decoded
    :param codebet: The scrambled alphabet used to encode the text
    :return decoded_word: The decoded word
    """
    decoded_word = ""
    for letter in text:
        index = codebet.index(letter)
        decoded_word += alpha[index]
    return decoded_word


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
