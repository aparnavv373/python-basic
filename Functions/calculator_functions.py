# function for addition
def add(num1,num2):
 return num1+num2

#function for subtraction
def subtract(num1,num2):
 return num1-num2

# function for multiplication
def multiply(num1,num2):
 return num1*num2

# function for division
def divide(num1,num2):
 if num2!=0:
    return num1/num2
 else :
    return "Error! division by zero"



num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Addition:",add(num1,num2))
print("Subtraction:",subtract(num1,num2))
print("Multiplication:",multiply(num1,num2))
print("Division:",divide(num1,num2))