def get_random_string(length):
    import random
    import string
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
