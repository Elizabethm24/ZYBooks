# convert decimal integer to Roman numerals

def roman_from_decimal(number : int) -> str:
    """Convert number (1-3999) to a Roman numeral.
    >>> roman_from_decimal(5)
    'V'
    >>> roman_from_decimal(10)
    'X'
    >>> roman_from_decimal(20)
    'XX'
    """
    ROMAN_LETTERS = { 1000: "M", 500: "D",
                      100: "C", 50: "L",
                      10: "X", 5: "V",
                      1: "I"}
    result = ""
    for value in ROMAN_LETTERS:
        how_many = number // value
        number %= value
        # TODO: finish this function!
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()