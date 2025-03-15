import random

def get_random_python_code():
    python_keywords = ["if", "else", "while", "for", "in", "return"]
    python_functions = ["print", "input", "len", "type", "sorted", "sum"]

    code = ""
    for i in range(random.randint(1, 10)):
        if random.random() < 0.5:
            code += python_keywords[random.randint(0, len(python_keywords) - 1)] + " "
        else:
            code += python_functions[random.randint(0, len(python_functions) - 1)] + "("
            for j in range(random.randint(1, 3)):
                code += str(random.randint(0, 10)) + ", "
            code = code[:-2] + ") "

    return code