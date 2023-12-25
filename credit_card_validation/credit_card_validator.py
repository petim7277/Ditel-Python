def collecting_user_input():
    userInput = input("Hello, Kindly Enter Card details to verify := \n")
    if userInput.isdigit():
        while len(userInput) != 16:
            print("\nCard number entered might be Incorrect !")
            userInput = input("Hello, Kindly Enter Card details to verify again := \n")
            return userInput


def multiplying_numbers():
    userInput = input(" ")
    one_digit = 0
    two_digit = 0
    for count in range(len(userInput)):
        if count % 2 == 0:
            result = count * 2
            if result < 9:
                one_digit += result
            if result > 9:
                two_digit += result % 10 + 1
    total = one_digit + two_digit
    return total


def summing_numbers_in_odd_positions():
    num_total = 0
    counter = 0
    userInput = input("Hello, Kindly Enter Card details to verify again := \n")
    for counter in range(len(userInput)):
        if counter % 2 != 0:
            num_total = num_total + int(userInput[counter])
    return num_total


def calculating_credit_card_validity():
    userInput = input("Hello, Kindly Enter Card details to verify again := \n")
    summation = multiplying_numbers() + summing_numbers_in_odd_positions()
    for count in range(len(userInput)):
        status = ""
    if summation % 10 == 0:
        status = "Card number is Valid"
    else:
        status = "Card number is Invalid"

    print("**********************************************")
    types = ""
    if userInput[0] == 4:
        types = " Visa card "
    elif userInput[0] == 5:
        types = " Master Card"
    elif userInput[0] == 6:
        types = " Discover Card"
    elif userInput[0 - 1] == 37:
        types = " American Express Card"
    else:
        types = "None"
    print(f"Credit Card Type : {types}")
    print(f"*** Card Number : {userInput}")
    print(f"*** Card Digit length : {count + 1}")
    print(f"*** Credit Card Validity Status : {status}")
    print("**********************************************")

# 43885760184026267
# 5399831619690404
# 4388576018410707
