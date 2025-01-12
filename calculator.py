# Simple Python Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Choose an operator (+ - * /): ")

if operator == "+":
    result = num1 + num2
    print (f"The result is {round(result, 3)}")
elif operator == "-":
    result = num1 - num2
    print (f"The result is {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print (f"The result is {round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print (f"The result is {round(result, 3)}")
else:
    print ("Please enter a valid operator")