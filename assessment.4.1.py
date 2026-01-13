# #1> print number from 1 to 10
# for i in range (1,11):
#     print (i)
    
# #2> Display multiplication table for a given number
# num = int(input("Enter a number:"))
# for i in range(1,11):
#     print (num ,"x", i ,"=", num*i)  
    
#  #3> Find factorial of a number
# num = int(input("Enter a number:"))
# fact  = 1
# for i in range (1, num+1):
#     fact = fact * i
#     print("factorial:", fact)
    
#  #4> Generate the first N Fibonacci numbers  
# n = int(input("Enter N:"))
# a=1
# b=2
# for i in range(n):
#     print(a, end= " ")
#     c=a+b
#     a=b
#     b=a 
    
#  #5> Check if a number is prime.
# num = int(input("Enter a number:"))
# if num<=1:
#      print(num, "is not a prime number")
# else:
#     for i in range(2,int(num ** 0.5) + 1):
#         if num % i == 0:
#           print(num, "not a prime number")
#           break
#     else:
#           print(num, "is a prime number") 
          
#  #6> Reverse a number (e.g., 123 → 321).
# num = int(input("Enter a number:"))
# rev = 0
# while num > 0:
#     rev = rev*10 + num%10
#     num = num // 10
#     print("Revesed number",rev)

                 
#  #7> Count digits in a number.
# num = int(input("Enter a number:"))
# count = 1
# while num > 0:
#      count += 1
#      num //= 10 
#      print("Number of Digits", count)
    
# #8> sum of even numbers between 1-100
# sum = 0
# for i in range (2,101,2):
#     sum += i
#     print("Sum of Even Numbers:",sum)
    
#9> Print a pyramid pattern.  
rows = 5
for i in range(1, rows + 1): 
        print("*" *i)
    
#10> Find all divisors of a number.
num = int(input("Enter number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        
             