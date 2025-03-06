import random
def get_random_string(length):
    """Generate a random string of letters and digits.
    :param length: The desired length of the string.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(letters) for i in range(length))