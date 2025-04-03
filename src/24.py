def calculate_average(numbers):
    if not numbers:
        return 0.0
    else:
        sum_numbers = sum(numbers)
        average = sum_numbers / len(numbers)
        return average

numbers = [1, 2, 3, 4]
average = calculate_average(numbers)
print(f"The average of the given numbers is: {average}")
