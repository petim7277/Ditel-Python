def average():
    user_input = 0
    add = 1
    for count in range(10):
        user_input = int(input("Enter your score: "))
        add = add + user_input
        average = add / count
        print("The average of ten scores entered is:"+ average)


print(average())
