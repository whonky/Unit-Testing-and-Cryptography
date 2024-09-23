import math

# Copy and paste any functions you need from the Affine assignment!
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def mod_inverse_helper(a, b):
    q, r = a // b, a % b
    if r == 1:
      return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)


def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


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


def convert_to_text(num, n):
    """
    Converts a ngram (a group of letters) that has been converted to a number back to text.
    The returned text will be in all uppercase.

    :param num: The number to be converted
    :param n: The number of letters in the ngram
    :return: The converted text
    """

    converted_text = ""
    number = num

    for i in range(n):
      index = number % 26
      number = number // 26
      converted_text += alpha[index]

    return converted_text


# Also write these:


def rsa_encode(text, m, e):
    """
    Encodes text using RSA encryption.
    The text should be in all uppercase and only include letters from the alphabet.
    :param text: The text to be encoded.
    :param m: Two extremely large prime numbers multiplied together. This is the modulus used when encoding/decoding.
    :param e: An encoding/decoding exponent
    :return: The encoded text, returned as a number
    """
    x = convert_to_num(text)
    if x < m:
        return pow(x, e, m)
    else:
        return "There was an error. The inputted text is too long."



def rsa_decode(num, m, d, l):
    """
    Decodes text that has been converted into a number with RSA encryption back to text.
    The text will be returned in all uppercase.
    :param num: The number to convert back to text
    :param m: Two extremely large prime numbers multiplied together. This is the modulus used when encoding/decoding.
    :param d: The totient of mod m, used to decode. Found using get_d function.
    :param l: The length of the original text.
    :return: The decoded text
    """
    decoded_num = pow(num, d, m)
    return convert_to_text(decoded_num, l)


def get_d(p, q, e):
    """
    Calculates d, an exponent used to decode text encrypted with RSA encryption.
    :param p: An extremely large prime number
    :param q: Another extremely large prime number
    :param e: An encoding/decoding exponent
    :return:
    """
    t = (p - 1) * (q - 1)
    return mod_inverse(e, t)


text = "THEFIVEBOXINGWIZARDSJUMPQUICKLY"
l = len(text)
p = 292361466231755597564095925310764764819
q = 307125506157764866722739041634199200019
e = 65537
m = p * q
d = get_d(p, q, e)
enc = rsa_encode(text, m, e)
dec = rsa_decode(enc, m, d, l)
print(enc)
print(dec)
# If this works, dec should be the same as text!

text = "HELLO"
l = len(text)
p = 531287
q = 939119
e = 65537
m = p * q
d = get_d(p, q, e)
enc = rsa_encode(text, m, e)
dec = rsa_decode(enc, m, d, l)
print(enc)
print(dec)

# Part 2: Generate your own key!

#from sympy import nextprime
from random import randint

def make_prime(n):
  lower = 2 ** (n - 1) + 1
  upper = 2 ** n - 1
  temp = randint(lower, upper)
  return nextprime(temp)




'''import math

# Copy and paste any functions you need from the Affine assignment!

# Also write these:
def rsa_encode(text, m, e):
  return 0

def rsa_decode(num, m, d, l):
  return ""

def get_d(p, q, e):
  return 0

text = "THEFIVEBOXINGWIZARDSJUMPQUICKLY"
l = len(text)
p = 292361466231755597564095925310764764819
q = 307125506157764866722739041634199200019
e = 65537
m = p * q
d = get_d(p, q, e)
enc = rsa_encode(text, m, e)
dec = rsa_decode(enc, m, d, l)
print(enc)
print(dec)
# If this works, dec should be the same as text!


# Part 2: Generate your own key!

from sympy import nextprime
from random import randint

def make_prime(n):
  lower = 2 ** (n - 1) + 1
  upper = 2 ** n - 1
  temp = randint(lower, upper)
  return nextprime(temp)

'''