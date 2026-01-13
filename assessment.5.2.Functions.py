#1> Function to check if a number is prime.
def is_prime(num):
    if num <=1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        return True
num = 6
if(is_prime):
    print("prime number")
else:
    print("not a prime number")        

#2> Function to reverse a string.
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev 
print(reverse_string("skytus"))    

#3> Function to find factorial.
def factorial(num):
    fact = 1
    for i in range(1,num + 1):
        fact *= i
    return fact
print(factorial(6))    

#4>Function to calculate simple interest.
def simple_interest(principal,rate,time):
    interest = (principal*rate*time)/100
    return interest
si = simple_interest(1000,5,2)
print("Simple Interest:", si)

#5> Function to check if a word is palindrome.
def is_palindrome(word):
    return word == word[::-1]
word = input(" Enter a word:")
if is_palindrome(word):
    print("palindrome")
else:
    print("Not a palindrome")    

#6> Function to count vowels in a string.
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in"aeiou":
            count += 1
    return count
word = input("Enter a string:")
print("Number of vowels:", count_vowels(word)) 

#7> Function to merge two lists.
def merge_lists(list1, list2):
    return list1 + list2
a=[1,2,3] 
b=[4,5,6]
print("Merged list:", merge_lists(a,b))         

#8> Function to find GCD of two numbers.
def gcd(a,b):
    while b !=0:
        a,b = b, a % b
    return a 
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("GCD:",gcd(num1, num2))    

#9> Function to find area of rectangle.
def area_of_rectangle(length, breadth):
    return length * breadth
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Area of rectangle:", area_of_rectangle(l, b))

#10>
def is_armstrong(num):
    temp = num
    total = 0
    digits = len(str(num))
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //=10
    return total == num
number = int(input("Enter a number: "))
if is_armstrong(number):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")            