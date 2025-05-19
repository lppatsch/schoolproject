def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
    return total

n = 5  # example: calculate the square of numbers from 1 to 5
result = sum_of_squares(n)
print(result)  # output will be the sum of squares from 1^2 to 5^2
