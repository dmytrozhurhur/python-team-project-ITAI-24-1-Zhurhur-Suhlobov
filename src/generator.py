import random
import string

def generate_password(length: int, use_uppercase: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Generates a password based on the given parameters.
    :param length: password length
    :param use_uppercase: whether to include uppercase letters
    :param use_digits: whether to include digits
    :param use_symbols: whether to include special characters
    :return: generated password
    """
    if length < 1:
        raise ValueError("Password length must be greater than zero.")

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected!")

    return ''.join(random.choice(characters) for _ in range(length))

def assess_strength(password: str) -> str:
    """
    Assesses the strength of a password based on its length and character variety.
    :param password: password to check
    :return: text evaluation of strength (Weak, Medium, Strong)
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score < 2:
        return "Weak"
    elif score < 4:
        return "Medium"
    else:
        return "Strong"