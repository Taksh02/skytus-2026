a = 10
b = 3

remainder = a % b
print("Remainder:", remainder)


#2> Check if a number is even or odd.///
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


#3> Compare two numbers and print the large one 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("The larger number is:", num1)
elif num2 > num1:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal")

#4> .Write a program to calculate the square and cube of a number.

num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square of the number:", square)
print("Cube of the number:", cube)

#5> Check if two entered numbers are equal.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 == num2:
    print("Both numbers are equal")
else:
    print("The numbers are not equal")

#6> Take two numbers and print True if both are positive, else False.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > 0 and num2 > 0:
    print(True)
else:
    print(False)

    
#7> Write a program to convert float to integer
num = float(input("Enter a float number: "))
num_int = int(num)
print("The integer value is:", num_int)

#8> Take a number as string, convert to int, and multiply by 10.
num_str = input("Enter a number: ")
num_int = int(num_str)
result = num_int * 10

print("Result:", result)

  
#9> Write a program that uses and & or operators to check multiple conditions.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

both_positive = num1 > 0 and num2 > 0
one_even = (num1 % 2 == 0) or (num2 % 2 == 0)
print("Both numbers are positive:", both_positive)
print("At least one number is even:", one_even)

#10> Divide two numbers and print the quotient and remainder separately.
num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))
quotient = num1 // num2
remainder = num1 % num2

print("Quotient:", quotient)
print("Remainder:", remainder)
