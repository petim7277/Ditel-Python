first_number = int(input("Enter a number : "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number : "))

sum = first_number + second_number + third_number
average = first_number + second_number + third_number/3
product = first_number * second_number * third_number
print("the sum of all three numbers is : ",sum)
print("the average of all three numbers is : ",average)
print("the product of all three numbers is : ",product)

if first_number > second_number and third_number:
	print("The largest number is : ",first_number)


if second_number >   third_number :
	print("The largest number is : ",second_number)


if third_number > first_number and second_number:
	print("The largest number is : ",third_number)



if first_number < second_number and third_number:
	print("The smallest number is : ",first_number)


if second_number <   first_number :
	print("The smallest number is : ",second_number)


if third_number < first_number and second_number:
	print("The smallest number is : ",third_number)
