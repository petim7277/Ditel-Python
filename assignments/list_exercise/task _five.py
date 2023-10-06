list_of_numbers = [15, 20, 25, 10, 10, 5]
duplicate = [0]
for index in list_of_numbers:
    if list_of_numbers[index] == duplicate[index]:
        duplicate = index
print(f"The duplicate removed from the list is = {duplicate}")
