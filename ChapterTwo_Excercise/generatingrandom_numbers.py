import random


counter = 0
while counter < 10:
    user_input = int(input("Enter a number between the range of 1 and 10 :"))
    _rand=(random.randint(1,10))
    if user_input == _rand and user_input < 10:
        print("you guessed right")

    counter += 1


