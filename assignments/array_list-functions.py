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
    smallest = len(user_input)

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
    user_input = int(input("Enter a number: "))


