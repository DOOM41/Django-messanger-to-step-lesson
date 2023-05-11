import random


def generate_code(code_size: int) -> str:
    digits = '0123456789'
    alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = digits + alfabet
    code = [symbols[random.randrange(0, len(symbols))] for _ in range(code_size)] # noqa

    return ''.join(code)
