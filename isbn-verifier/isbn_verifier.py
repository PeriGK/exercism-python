def verify(isbn):
    import re
    sum_digits = 0
    isbn = re.sub('[-]', '', isbn)

    # If the length of the isbn is not 10. If 'x' is contained it should be the last one
    if len(isbn) != 10 or (isbn.lower().find('x') not in [9, -1]):
        return False

    multiplier = 10
    for isbn_digit in isbn:
        if isbn_digit == 'X':
            isbn_digit = 10
        elif isbn_digit.isalpha():
            return False
        sum_digits += int(isbn_digit) * multiplier
        multiplier = multiplier - 1

    return sum_digits % 11 == 0

# print(verify(0))