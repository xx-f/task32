import random
import string


def generate_password(length=8):
    """
    Генерирует случайный пароль из букв (верхний и нижний регистр), цифр и спецсимволов.
    plength: длина пароля (по умолчанию 8)
    return: строка с паролем
    """


    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password