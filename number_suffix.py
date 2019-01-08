def number_suffix(number):
    number = str(round(number))

    ones_digit = str(number)[-1]
    tens_digit = str(number)[-2]

    if tens_digit == '1':
        suffix = 'th'
    elif ones_digit == '1':
        suffix = 'st'
    elif ones_digit == '2':
        suffix = 'nd'
    elif ones_digit == '3':
        suffix = 'rd'
    else:
        suffix = 'th'
    return number + suffix
