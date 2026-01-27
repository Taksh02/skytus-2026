#1> Write a program to handle division by zero error.
try:
    a = int(input("Enter a numerator:"))
    b = int(input("Enter denominator:"))
    result = a/b
    print("Result:", result)
except zeroDivisonError:
    print("Error: Cannot divide by zero")    

  #2> Write a program to handle invalid integer input.
try:
    num = int(input("Enter a number:"))
    print("you entered:", num)
except ValueError:
    print("Error: please enter a valid integer")      

   #3> Write a program to open a file and handle the “file not found” error.
try:
    file = open("data.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found")     

  #4>Write a program to demonstrate multiple exception blocks.
try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero") 
except ValueError:
    print("Invalid input")         

#5> Write a program to use finally for resource cleanup.
try:
    file = open("data.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file (if opened)") 
    
#6> Write a program to create a custom exception for invalid age (<18).
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter age:"))
    if age < 18:
        raise InvalidAgeError
    print("Access granted")
except InvalidAgeError:
    print("Error: Age must be 18 or above")         

#7> Write a program to handle IndexError when accessing a list.
try:
    my_list = [10,20,30]
    print(my_list[5])
except IndexError:
    print("Error: Index out of range")          

#8> Write a program that takes two numbers and handles all possible errors.
try:
    a = int(input("Enter First number:"))
    b = int(input("Enter second number:"))
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division by Zero not allowed")
except Exception:
    print("something went wrong")   

 #9> Write a program to log errors to a file instead of printing them
import logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except Exception as e:
    logging.error(e)

#10> Write a program that validates an email forma
try:
    email = input("Enter email:")
    if "@" not in email or "." not in email:
        raise ValueError
    print("valid email")
except ValueError:
    print("Invalid email format")            