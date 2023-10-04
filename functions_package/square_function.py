def the_square_function(number):
    """this function calculates the square of any number given """
    if number > 0:
        result = number * number
        return result


print(f"the square of number entered is:", the_square_function(1))


def the_add_function(*number):
    """This function calculates the sum of numbers given"""
    for count in number:
        count = count + number
        return count


print(f"sum of number or numbers entered is: ", the_add_function())


def the_multiplication_function(number):
    result = 1
    for count in range(1, 13):
        result = count * number
    return result


print(the_multiplication_function(5))


def the_maximum_function(number_one, number_two, number_three):
    maximum_value = number_one
    if number_two > maximum_value:
        maximum_value = number_two
    if number_three > maximum_value:
        maximum_value = number_three
        return maximum_value


print(f"The maximum value is: ", the_maximum_function(34, 56, 51))
