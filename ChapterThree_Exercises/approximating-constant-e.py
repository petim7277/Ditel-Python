user_input = 0
highest = user_input
second_highest = 0
for count in range(11):
    user_input = int(input("Enter a number: "))
    if user_input == highest:
        print(f"highest  = {count}")
    elif user_input != highest:
        print(f"second highest  = {count}")

# still figuring  this out
