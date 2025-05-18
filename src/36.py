def add_two_numbers(a, b):
    return a + b

def subtract_two_numbers(a, b):
    return a - b

def multiply_two_numbers(a, b):
    return a * b

def divide_two_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def check_function(func_name, args=()):
    def _check():
        result = func_name(*args)
        print(f"{func_name} was called with {args}. The result is {result}")
    
    _check()

add_two_numbers(10, 20) 
subtract_two_numbers(5, 3) 
multiply_two_numbers(4, 6)  
divide_two_numbers(10, 0)
