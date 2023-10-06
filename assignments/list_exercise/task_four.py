list_of_numbers = [15, 20, 25, 20, 10,5]
smallest = list_of_numbers[4]
for index in list_of_numbers:
    if index < smallest:
        smallest = index
print(f"The smallest element in the list is = [{smallest} ]")
