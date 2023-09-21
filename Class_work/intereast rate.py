user_input = float(input(" Enter your investment amount : "))
for interest in range(1, 31):
    deposit = user_input * 0.10
    new_interest = deposit + user_input
    user_input = new_interest
    print(f"first interest {deposit:.2f} current interest rate is :{new_interest} for year {interest}")


