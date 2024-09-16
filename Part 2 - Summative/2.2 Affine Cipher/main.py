import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    """
    Encodes text with an affine cipher.

    :param text: The text to be encoded.
    :param a: The number multiplied by the letter's index. Should be less than 26 and share no common factors with the number 26.
    :param b: The number added as a shift. Should be less than 26.
    :return: The encoded text.
    """

    encoded_text = ""
    text = str(text)

    for letter in text:
        if letter.isalpha():
            index = alpha.find(letter.upper())
            encoded_index = (a * index + b) % len(alpha)
            if letter.islower():
                encoded_text += alpha[encoded_index].lower()
            else:
                encoded_text += alpha[encoded_index]
        else:
            encoded_text += letter

    return encoded_text

def affine_decode(text, a, b):
    """
    Decodes text with an affine cipher.

    :param text: The text to be decoded.
    :param a: The number multiplied by the letter's index. Should be less than 26 and share no common factors with the number 26.
    :param b: The number added as a shift. Should be less than 26.
    :return: The decoded text.
    """

    decoded_text = ""
    text = str(text)

    for letter in text:
        if letter.isalpha():
            index = alpha.find(letter.upper())
            decoded_index = index - b
            decoded_index = (mod_inverse(a, len(alpha)) * decoded_index) % len(alpha)
            if letter.islower():
                decoded_text += alpha[decoded_index].lower()
            else:
                decoded_text += alpha[decoded_index]
        else:
            decoded_text += letter

    return decoded_text

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    """
    Converts a group of letters (a ngram) to numbers.
    Characters not in the alphabet in ngram are skipped and ignored.

    :param ngram: A string of letters
    :return: The converted numbers
    """

    converted_ngram = 0
    ngram_index = 0

    for i in range(len(ngram)):
        if ngram[i].upper() in alpha:
            alpha_index = alpha.find(ngram[i].upper())
            converted_ngram += alpha_index * 26 ** ngram_index
            ngram_index += 1

    return converted_ngram

def convert_to_text(num):
    """
    Converts a ngram (a group of letters) that has been converted to a number back to text.
    The returned text will be in all uppercase.

    :param num: The number to be converted
    :return: The converted text
    """

    converted_text = ""
    number = num

    while number > 0:
        index = number % 26
        number = number // 26
        converted_text += alpha[index]

    return converted_text

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    return ''

def affine_n_decode(text, n, a, b):
    return ''

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!