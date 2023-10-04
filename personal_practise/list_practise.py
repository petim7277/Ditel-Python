def list_add_function():
    total = 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for count in numbers:
        total = total + count
    # print(total)
    return total


def list_product_function():
    product = 1
    numbers = [1, 2, 3, 4, 5]
    for count in numbers:
        product = product * count
    # print(product)
    return product


def list_largest_element_function():
    largest = 0
    numbers = [10, 20, 30, 40, 50, 60, 70]
    for count in numbers:
        if count > largest:
            largest = count
            print(largest)
    return largest


if __name__ == '__main__':
    list_add_function()
    list_product_function()
    print(list_largest_element_function())
