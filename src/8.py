import random

def get_random_code():
    num = random.randint(0, 9)
    str = ""
    for i in range(num):
        str += chr(random.randint(65, 90))
    return str

get_random_code()
