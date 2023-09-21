userInput = float(input("Enter investment amount : "))
for count in range(1, 31):
    deposit = userInput * 0.10
    investment_return = deposit + userInput
    current_return = investment_return
    print(f"first interest return{deposit}\t\t New investment return{current_return}\t\t for year{count}")
