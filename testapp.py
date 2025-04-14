import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("Должен быть выбран хотя бы один набор символов")
    
    if length < 1:
        raise ValueError("Длина пароля должна быть не менее 1 символа")
    
    return ''.join(random.choice(characters) for _ in range(length))

print(generate_password())