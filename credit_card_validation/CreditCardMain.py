import credit_card_validator

if __name__ == '__main__':
    print("jog",print("gog"))

    def print_stream():
        credit_card_validator.collecting_user_input()
        userInput = input("Hello, Kindly Enter Card details to verify again := \n")
        cards = 0
        count = 0
        for count in range(len(userInput)):
            cards += int(userInput[count])
        print("**********************************************")
        card_types = int(userInput[0])
        if card_types == 4:
            types = " Visa card "
        elif card_types == 5:
            types = " Master Card"
        elif card_types == 6:
            types = " Discover Card"
        elif card_types == 37:
            types = " American Express Card"
        else:
            types = "None"
        print(f"Credit Card Type : {types}")
        print(f"*** Card Number : {userInput}")
        print(f"*** Card Digit length : {count + 1}")
        print(f"*** Credit Card Validity Status : {credit_card_validator.calculating_credit_card_validity()}")
        print("**********************************************")
