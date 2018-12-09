def is_armstrong(number):
    num_digits = len(str(number))
    sums = 0
    for digit in str(number):
        sums += int(digit) ** num_digits

    return sums == number