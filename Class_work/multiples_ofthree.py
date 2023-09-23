
for multiples in range(1, 51):

    if multiples % 3 == 0 and multiples % 5 == 0:
        print("FizzBuzz")
    elif multiples % 3 == 0:
        print("Fizz")
    elif multiples % 5 == 0:
        print("Buzz")
    else:
        print(multiples)

numbers = 1
while numbers < 51:
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)
    numbers += 1
