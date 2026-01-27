#1> Check if a person is eligible to vote
age = int(input("Enter a number:"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
#2> Grade calculator based on marks
marks = int(input("Enter a marks:"))
if marks >= 90:
   print("Grade A")
elif marks >=80:
    print("Grade B") 
else: 
    print("Grade C")   

#3> Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
colour = input("Enter traffic light colour:")
if colour == "red":
    print("stop")
elif colour == "yellow":
    print("wait")
elif colour == "Green":
    print("Go") 
else:
    print ("invalid colour")   

#4> ATM withdrawal check: sufficient balance or not.
balance = 20000
amount = int(input("Enter a withdrawal amount:"))
if amount <= balance:
    print("withdrawal successful")
else:
    print("insufficient balance")   
    
#5> Check if a number is positive, negative, or zero.
num = int(input("Enter a number:"))
if num > 0:
    print ("Positive")
elif num < 0:
    print ("negative")
else:
    print ("Zero")    
                           
   #6> Check if a number lies within a given range.
  num = int(input("Enter number: "))

if num >= 10 and num <= 50:
    print("Number is in range")
else:
    print("Number is out of range")

   #7> Username & password verification.
username = input("Enter a username: ")
password = input("Enter a password: ")
if username == "admin" and password == "2304":
    print("login successful")
else:
    print("invalid username or password") 
    
  #8> Electricity bill calculator based on units consumed.
units = float(input("Enter units: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("Electricity Bill:", bill)

 #9> Simple calculator (add, subtract, multiply, divide).
a = float(input("Enter First Number:"))
b = float(input("Enter Second Number:"))
op = input("Enter operator(+,-,*,/): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")
    
 #10> Check type of triangle (equilateral, isosceles, scalene).
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
   
     
   
                         