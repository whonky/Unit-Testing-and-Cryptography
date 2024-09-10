# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"


def vig_encode(text, keyword):
    """
    Encodes given text with a vigenere cipher using the given keyword.

    Spaces are read and returned as underscores.
    Special characters and numbers in the text are omitted.
    The encoded text will be all capital letters regardless of original capitalization.
    :param text:
    :param keyword:
    :return:
    """

    encoded_word = ""
    simplified_text = ""
    simplified_keyword = ""
    text = str(text)

    for letter in text:
        if letter.isalpha():
            simplified_text += letter.upper()
        elif letter == "_" or letter == " ":
            simplified_text += "_"

    for letter in keyword:
        if letter.isalpha():
            simplified_text += letter.upper()
        elif letter == "_" or letter == " ":
            simplified_text += "_"

    for i in range(len(simplified_text)):
        text_index = alpha.index(text[i])
        keyword_index = alpha.index(keyword[i % len(keyword)])
        encoded_index = keyword_index + text_index
        encoded_word += alpha[encoded_index % len(alpha)]

    return encoded_word


def vig_decode(text, keyword):
    decoded_word = ""
    for i in range(len(text)):
        alpha_index = alpha.index(text[i])
        keyword_index = alpha.index(keyword[i % len(keyword)])
        decoded_index = alpha_index - keyword_index
        decoded_word += alpha[decoded_index % len(alpha)]
    return decoded_word


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!