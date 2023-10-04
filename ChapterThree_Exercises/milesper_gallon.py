# def calculating_miles_per_gallon():
print("Enter -1 to stop the operation")
user_input = 0
second_user_input = 0
total_miles_driven = 1
total_gallons_used = 1
total_miles_and_gallons_used= 1
while user_input != -1 and second_user_input != -1:
    user_input = float(input("Enter miles driven: "))
    second_user_input = int(input("Enter gallons used: "))
    total_miles_driven = total_miles_driven + user_input
    total_gallons_used = total_gallons_used + second_user_input
    total_miles_and_gallons_used = total_miles_driven / total_gallons_used
print(f"sum of miles driven is : {total_miles_driven}")
print(f"sum of gallos used is : {total_gallons_used}")
print(f"combined miles per gallon is : {total_miles_and_gallons_used}")
