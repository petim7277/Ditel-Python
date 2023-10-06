def array_list_solving_largest_element():
    largest = 0
    user_input = [1, 20, 30, 40, 50]
    for index in user_input:
        if index > largest:
            largest = index

    return largest


# print(array_list_solving_largest_element())


def array_list_solving_smallest_element():
    user_input = [30, 40, 10, 50, 20]
    smallest = user_input

    for index in user_input:
        if index < smallest:
            smallest = index
    return smallest


# print(array_list_solving_smallest_element())


def array_list_concatenation():
    first_input = [10, 20, 30, 40, 50]
    second_input = [60, 70, 80, 90, 100]
    result = first_input + second_input
    return result


# print(array_list_concatenation())


def array_function_that_return_number_in_list():
    user_input = str(input("Enter a number: "))
    for index in user_input:
        result = int(user_input[index])
    return result


# print(f"numbers in list is =={array_function_that_return_number_in_list()}")


def array_list_that_prints_odd_positions_in_list():
    list_of_numbers = [1, 2, 3, 4, 5]
    odd_index = 0
    for index in list_of_numbers:
        if index % 2 != 0:
            odd_index = odd_index + index
            print(odd_index)
        return odd_index


# print(f"The odd positions in this list is = {array_list_that_prints_odd_positions_in_list()}")


def array_list_that_prints_even_position_in_list():
    list_of_number = [1, 2, 3, 4, 5]
    even_index = 0
    for index in list_of_number:
        if index % 2 == 0:
            even_index = index
            return even_index


# print(f"The even positions in  this list is = |{array_list_that_prints_even_position_in_list()}|")


def array_list_that_combines_two_list():
    lists_one = [1, 2, 3, 4, 5]
    lists_two = ['a', 'b', 'c', 'd', 'e']
    for index in lists_two:
        combine = lists_one, lists_two

    return combine


print(array_list_that_combines_two_list())


