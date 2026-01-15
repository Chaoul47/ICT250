import string
from gcd_utils import gcd   

def mod_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i
    return None


def affine_cipher(text, a, b, mode):
 
    if gcd(a, 26) != 1:
        return "Invalid key: gcd(a, 26) must be 1"

    result = ""
    text = text.upper()

    if mode == "decrypt":
        a_inv = mod_inverse(a)

    for char in text:
        if char in string.ascii_uppercase:
            x = ord(char) - ord('A')

            if mode == "encrypt":
                y = (a * x + b) % 26
            else:
                y = (a_inv * (x - b)) % 26

            result += chr(y + ord('A'))
        else:
            result += char

    return result

text = input("Enter message: ")
a = int(input("Enter key a: "))
b = int(input("Enter key b: "))
mode = input("Encrypt or decrypt? ").lower()

print("Result:", affine_cipher(text, a, b, mode))
