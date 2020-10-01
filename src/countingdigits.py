def count_digits(num):
    """function to count the number of digits in a number"""
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


print(count_digits(1))