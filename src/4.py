import random

def get_random_code(length=10):
    code = ""
    while len(code) < length:
        code += str(random.randint(10**5, 10**6 - 1))
    return code