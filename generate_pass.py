import random
import string

import click

# @click.command()
# @click.option(
#     "--length", default=8, help="Specify the length of the password (default : 8)"
# )
# @click.option(
#     "--uppercase",
#     is_flag=True,
#     help="Include uppercase character (A-Z)",
# )
# @click.option(
#     "--lowercase",
#     is_flag=True,
#     help="Include lowercase character (a-z)",
# )
# @click.option("--numbers", is_flag=True, help="Include numbers (0-9)")
# @click.option("--symbols", is_flag=True, help="Include symbols (!,@,#,etc...)")


def generate_pass(length, uppercase, lowercase, numbers, symbols):
    chars = []
    characters_pool = ""

    if uppercase:
        characters_pool += string.ascii_uppercase
    if lowercase:
        characters_pool += string.ascii_lowercase
    if numbers:
        characters_pool += string.digits
    if symbols:
        characters_pool += string.punctuation

    if length > 0:
        for _ in range(length):
            get_chars = random.choices(characters_pool)[0]
            chars.append(get_chars)
    else:
        print("Length cannot be 0")

    password = "".join(chars)

    print(f"\n{password}")
