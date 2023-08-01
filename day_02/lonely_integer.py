def lonelyinteger(a):
    repeated_numbers = sorted(a)
    unique_numbers = []
    for number in a:
        if number not in unique_numbers:
            unique_numbers.append(number)
            repeated_numbers.remove(number)
        lonely_integer = [unique_number for unique_number in unique_numbers if unique_number not in repeated_numbers]
    return lonely_integer[0]