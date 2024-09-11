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
    :param a:
    :param b:
    :return:
    """

    encoded_text = ""
    text = str(text)

    for letter in text:
        index = alpha.find(letter)
        encoded_index = (a * index + b) % len(alpha)
        encoded_text += alpha[encoded_index]

    return encoded_text

def affine_decode(text, a, b):
    """
    Decodes text with an affine cipher.
    :param text: The text to be decoded.
    :param a:
    :param b:
    :return:
    """

    decoded_text = ""
    text = str(text)

    for letter in text:
        index = alpha.find(letter)
        decoded_index = index - b
        decoded_index = (mod_inverse(a, len(alpha)) * decoded_index) % len(alpha)
        decoded_text += alpha[decoded_index]

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
    return 0

def convert_to_text(num, n):
    return ''

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
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