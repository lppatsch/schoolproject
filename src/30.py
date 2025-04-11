def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot divide by an empty list")
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

if __name__ == "__main__":
    try:
        print("Average of the given list: ", calculate_average([1, 2, 3, 4, 5]))
    except ValueError as e:
        print(e)
