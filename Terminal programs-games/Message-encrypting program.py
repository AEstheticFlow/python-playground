import string
import random

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
print(f"chars: {chars}\n")

key = chars.copy()
random.shuffle(key)
print(f"key: {key}\n")
# ****************************************************************************** #

# Encrypt:
print('*' * 30)
plain_text = input("Enter a message to encrypt: ")
encrypted_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]

print(f"Encrypted message: {encrypted_text}")

# -------------------------------------------------------------------------------- #

# Decrypt
print('*' * 30)
encrypted_text = input("Enter a message to decrypt:")
plain_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Decrypted message: {plain_text}")
print('*' * 30)


# https://www.youtube.com/watch?v=vsLBErLWBhA