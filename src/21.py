import random

def simple_random_string(length):
    """Generate a random string of specified length."""
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

random_str = simple_random_string(10)
print(random_str)
