# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def factors(number):
    """
    This function calculates prime factors of a number and returns the last (biggest) value.
    """
    current_factor = 2

    while number > 1:

        if number % current_factor == 0:
            number = number / current_factor

        else:
            current_factor += 1

    return current_factor


print(factors(600851475143))
