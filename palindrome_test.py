def palindrome_test(in_string, bad_chars):
    """
    Find if the inputted word is a palindrome
    :param in_string:
    :param bad_chars:
    :return:
    """
    # Reconstruct input string without bad characters or spaces (only letters)
    letter_string = "".join([char for char in in_string.lower() if char not in bad_chars])
    letter_string = letter_string.replace(" ", "")

    # Determine if string of letters is a palindrome
    return letter_string == letter_string[::-1]
