user_input = 0
for count in range(1):
    first_input = int(input("Enter a number :"))
    second_input = int(input("Enter a number :"))
    third_input = int(input("Enter a number :"))
    fourth_input = int(input("Enter a number :"))
    add = first_input + second_input + third_input + fourth_input
    product = first_input * second_input * third_input * fourth_input
    average = first_input+second_input+third_input+fourth_input / 4
    if first_input > second_input and first_input > third_input and first_input > fourth_input:
        print(f"({first_input}) First number entered is the largest")
    elif second_input > first_input and second_input > third_input and second_input > fourth_input:
        print(f"({second_input}) Second number entered is the largest")
    elif third_input > first_input and third_input > second_input and third_input > fourth_input:
        print(f"({third_input}) Third entered is the largest")
    elif fourth_input > first_input and fourth_input > second_input and fourth_input > third_input:
        print(f"({fourth_input}) fourth entered is the largest")
    elif first_input < second_input and first_input < third_input and first_input < fourth_input:
        print(f"first number entered is the smallest :{first_input}")
    elif second_input < first_input and second_input < third_input and second_input < fourth_input:
        print(f"Second entered is the smallest:{second_input}")
    elif third_input < first_input and third_input < second_input and third_input < fourth_input:
        print(f"third number is  smallest{third_input}")
    elif fourth_input < first_input and fourth_input < second_input and fourth_input < third_input:
        print(f"fourth number entered is the fourth :{fourth_input}")
    else:
        print("Invalid input can't tell which is largest or smallest")

    print(f"Addition ={add}\t\t Product ={product}\t\t Average={average}")
