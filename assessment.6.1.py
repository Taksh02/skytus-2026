# class car:
#     def __init__(self,brand,model,speed=0):
#         self.brand = brand
#         self.model = model
#         self.speed = speed
#     def accelerate(self,increase):
#         self.speed += increase
#         print("speed after accelerating:",self.speed)
#     def brake(self,decrease):
#         self.speed -= decrease
#         if self.speed < 0:
#             self.speed = 0
#         print("Speed after braking:", self.speed)
# car1 = car("Toyota", "Fortuner")
# car1.accelerate(20)
# car1.brake(5)                    
    
# # create a bankaccount class with deposit and withdraw methods:
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         print("Deposit amount:", amount)
#         print("Current balance:", self.balance)
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdraw amount:", amount)
#             print("Current balance:",self.balance)
#         else:
#             print("Insufficient balance")
# account1 = BankAccount("Taksh",2000)
# account1.deposit(100)
# account1.withdraw(200)
# account1.withdraw(2000) 

# # Create a Student class with a method to calculate average marks
# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def calculate_average(self):
#         average = sum(self.marks)/len(self.marks)
#         return average 
# student1 = student("Taksh",[65,78,90])
# avg = student1.calculate_average()
# print("Average Marks:",avg)       
        
# #Create a Rectangle class with methods to find area and perimeter
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width 
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2 * (self.length + self.width)
# rect1 = Rectangle(5,3)
# print("Area of Rectangle:", rect1.area())
# print("Perimeter of Rectangle:", rect1.perimeter())             

# #Create an Employee class that displays salary details
# class employee:
#     def __init__(self,emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary
#     def display_salary(self):
#         print("Employee ID:",self.emp_id)
#         print("Employee Name:", self.name)
#         print("Salary:", self.salary)
# emp1 = employee(101, "Taksh", 35000)
# emp1.display_salary()           

# #Create a Book class to store title, author, and price, and display details
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display_details(self):
#         print("Book Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)
# book1 = Book("Python Programming", "Guido van Rossum", 499)
# book1.display_details()

# # Create a Book class to store title, author, and price, and display details.
# class Book:
#     def __init__(self,title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display_details(self):
#         print("Title:", self.title)
#         print("Author:",self.author)
#         print("price:", self.price)
# book1 = Book("Clean code","Robert c. Martin",551)
# book1.display_details()        
 
# #Create a Circle class to find area and circumference
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
#     def circumference(self):
#         return 2 * math.pi * self.radius
# circle1 = Circle(7)
# print("Area of Circle:", circle1.area())
# print("Circumference of Circle:", circle1.circumference())

# #Create a Laptop class with a method to apply discounts on price.
# class Laptop:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#     def apply_discount(self,discount_percent):
#         discount_amount = self.price * (discount_percent / 100)
#         self.price -= discount_amount
#         print("Price after discount:",self.price)
# laptop1 = Laptop("Dell", 60000)
# laptop1.apply_discount(10)

# #Create a Flight class with seat booking functionality. 
# class Flight:
#     def __init__(self, flight_number, total_seats):
#         self.flight_number = flight_number
#         self.total_seats = total_seats
#     def book_seat(self):
#         if self.total_seats > 0:
#             self.total_seats -= 1
#             print("Seat booked successfully.")
#             print("Seats remaining:", self.total_seats)
#         else:
#             print("No seats available.")
# flight1 = Flight("AI202", 3)
# flight1.book_seat()
# flight1.book_seat()
# flight1.book_seat()
# flight1.book_seat()

#Create a Shop class with a method to add and list products
class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products = []
    def add_product(self, product):
        self.products.append(product)
        print("Product added:", product)
    def list_products(self):
        print("\nProducts available in", self.shop_name)
        for product in self.products:
            print(product)
my_shop = Shop("Smart Store")
my_shop.add_product("Laptop")
my_shop.add_product("Mobile")
my_shop.add_product("Headphones")
my_shop.list_products()


           