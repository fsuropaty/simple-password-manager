import random
import string


def generate_pass(length, uppercase, lowercase, numbers, symbols):
    chars = []
    symbols_pool = "~!@#$%^&*()-_+=[]{};:<>,.?|"
    characters_pool = ""

    if uppercase:
        characters_pool += string.ascii_uppercase
    if lowercase:
        characters_pool += string.ascii_lowercase
    if numbers:
        characters_pool += string.digits
    if symbols:
        characters_pool += symbols_pool

    if length > 0:
        for _ in range(length):
            get_chars = random.choices(characters_pool)[0]
            chars.append(get_chars)
    else:
        print("Length cannot be 0")

    password = "".join(chars)

    return password
