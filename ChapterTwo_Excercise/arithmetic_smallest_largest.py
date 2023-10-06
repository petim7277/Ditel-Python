first_input = int(input("Enter a number: "))
second_input = int(input("Enter a number: "))
third_input = int(input("Enter a number: "))
sum_of_numbers = first_input + second_input + third_input
product_of_numbers = first_input * second_input * third_input
average_of_numbers = sum_of_numbers / 3
largest = 0
smallest = 0
if first_input > second_input and first_input > third_input:
    largest = first_input
    print("The first number entered is the largest")
elif first_input < second_input and first_input < third_input:
    smallest = first_input
    print("The first number entered is the smallest")

elif second_input > first_input and second_input > third_input:
    largest = second_input
    print("The first second number entered is the largest")
elif second_input < first_input and second_input < third_input:
    smallest = second_input
    print("The first second number entered is the smallest")
elif third_input > first_input and third_input > second_input:
    largest = third_input
    print("The third number entered is the largest")
elif third_input < first_input and third_input < second_input:
    smallest = third_input
    print("The third number entered is the smallest")
print(f"The sum of numbers entered is = {sum_of_numbers}")
print(f"The product of numbers entered is = {product_of_numbers}")
print(f"The average of numbers entered is = {average_of_numbers}")

