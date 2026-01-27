#Create a base class Animal and subclasses Dog and Cat.
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("car meows")
dog = Dog()
cat = Cat()
dog.speak()
cat.speak() 

#2>Create a class hierarchy for Vehicle → Car → ElectricCar
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class car(Vehicle):
    def drive(self):
        print("car is driving")
class ElectricCar(car):
    def charge(self):
        print("Electric car is charging")
ecar = ElectricCar()
ecar.start()
ecar.drive()
ecar.charge()                              

#3> Implement method overriding in a base and derived class
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def start(self):
        print("Car is starting")
v = Vehicle()
c = Car()
v.start()
c.start()

#4>Demonstrate multiple inheritance with two parent classes
class Father:
    def skill1(self):
        print("Father: Driving")
class Mother:
    def skill2(self):
        print("Mother: Cooking")
class Child(Father,Mother):
    def skill3(self):
        print("Child: playing cricket")
child = Child()
child.skill1()
child.skill2()
child.skill3() 

#5>Create a polymorphic function that works with different shapes
class circle:
    def draw(self):
        print("Drawing a circle")
class Rectangle:
    def draw(self):
        print("Drawing a Rectangle")
class Triangle:
    def draw(self):
        print("Drawing a Triangle")
def draw_shape(shape):
    shape.draw()
draw_shape(circle())
draw_shape(Rectangle())
draw_shape(Triangle()) 

#6> Create a Bank system with SavingsAccount and CurrentAccount classes.
class BankAccount:
    def calculate_interest(self):
        print("Interest calculation for bank account")
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account Interest Rate: 4%")
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account Interest Rate: 0%")
savings = SavingsAccount()
current = CurrentAccount()
savings.calculate_interest()
current.calculate_interest()                    

#7>  Create a class with private attributes and getter/setter methods.                                                                            
class person:
    def __init__(self):
        self._age = 0
    def set_age(self,age):
        self._age = age
    def get_age(self):
        return self._age 
p = person()
p.set_age(21)
print("Age:",p.get_age())          

#8> Create a Teacher and Student class to show inheritance.
class Teacher:
     def teach(self):
         print("Teacher is teaching")         
class Student(Teacher):
    def study(self):
        print("Student is studying")
s = Student()
s.teach()
s.study()   

#9> Create a MusicPlayer class and subclass Spotify to override play method
class MusicPlayer:
    def play(self):
        print("Playing music")
class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")
player = Spotify()
player.play()

#10> Demonstrate the use of super() in inheritance.
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def start(self):
        super().start()   
        print("Car is starting")
c = Car()
c.start()
 
               