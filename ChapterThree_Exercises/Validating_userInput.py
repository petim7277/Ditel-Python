userInput = int(input("Enter a number to continue operation  and -1 to stop:"))
positive_number = 0
negative_number = 0
counter = 0
while userInput != -1:
    counter += 1
    if userInput < 3:
        positive_number += 1
    else:
        negative_number += 1

    userInput = int(input("Enter a number to continue operation :"))

print("Operation ended")
print(f"Sum of positive numbers entered is: {positive_number}")
print(f"Sum of negative numbers entered is: {negative_number}")
