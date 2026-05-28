import random
import string

def generate_password(length: int, use_uppercase: bool, use_digits: bool, use_symbols: bool) -> str:
    
    if length < 1:
        raise ValueError("Довжина пароля має бути більше нуля.")

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Необхідно вибрати хоча б один набір символів!")

    return ''.join(random.choice(characters) for _ in range(length))

def assess_strength(password: str) -> str:

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
        return "Слабкий"
    elif score < 4:
        return "Середній"
    else:
        return "Надійний"