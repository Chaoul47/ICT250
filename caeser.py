import string
import utils
import gcd
def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char in string.ascii_uppercase:
            shifted_index = (ord(char) - ord('A') + shift) % 26
            result += chr(shifted_index + ord('A'))
        else:
            result += char
    return result


text = input("Enter message (UPPERCASE): ")
shift = int(input("Enter shift key: "))
mode = input("Enter mode (encrypt/decrypt): ").lower()

output = caesar_cipher(text, shift, mode)
print("Result:", output)
