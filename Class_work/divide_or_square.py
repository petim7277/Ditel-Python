import math


def squareroot_remainder(number):
    if number % 5 == 0:
        total = number ** 0.5
        return total
    elif number % 5 != 0:
        result = number % 5
        return result


print((squareroot_remainder(625)))
