#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15

num1 = int(input("please enter 1st number:  "))
num2 = int(input("please enter 2nd number:  "))
num3 = input("please enter an operator +, -, *, /:  ")
if num3 == '+':
	y = num1 + num2
elif num3 =='-':
	y = num1 - num2
elif num3 =='*':
	y = num1 * num2
else:
	y = num1/num2
	
print (y)


