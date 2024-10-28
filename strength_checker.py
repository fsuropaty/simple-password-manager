import string


def strength_checker(pswrd):
    score = 1
    pswrd_len = len(pswrd)

    if pswrd_len >= 12:
        score += 2
    elif pswrd_len >= 8:
        score += 1

    has_uppercase = any(char in string.ascii_uppercase for char in pswrd)
    has_lowercase = any(char in string.ascii_lowercase for char in pswrd)
    has_number = any(char in string.digits for char in pswrd)
    has_symbols = any(char in string.punctuation for char in pswrd)

    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_number:
        score += 1
    if has_symbols:
        score += 1

    return result(score)


def result(score):
    if score >= 6:
        return "You have strong password"

    if score <= 5:
        return "You have medium strength password"

    if score < 4:
        return "You have weak password"
