# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vig_encode(text, keyword):
    encoded_word = ""
    for i in range(len(text)):
        text_index = alpha.index(text[i])
        keyword_index = alpha.index(keyword[i % len(keyword)])
        encoded_index = keyword_index + text_index
        encoded_word += alpha[encoded_index % len(alpha)]
    return encoded_word


def vig_decode(text, keyword):
    return ""


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!