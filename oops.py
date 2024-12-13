#oops question

#Create a base class Animal with methods speak() and walk(). Create a derived class Dog
#that overrides the speak() method to print "Bark"
'''class Animal:
    def speak(self):
        print("Speak function of Animal")

    def walk():
        print("walk")
class dog(Animal):
    def speak(self):
        print("bark")
obj=dog()
obj.speak()'''

#Create a class BankAccount with private attributes _balance and a method deposit() to add money.
#Add another method get_balance() to access the balance.
'''class BankAccount():
    def __init__(self):
        print("Account created")
        self.balance=0
        self.a=int(input("enter the amount to add money"))
    def deposit(self):
        self.balance +=self.a
        if(self.balance>0):
            print(f"Deposited: {self.a}")
        else:
            print("Invalid deposit amount.Please enter the posotive amount")
    def get_balance(self):
        return self.balance

obj=BankAccount()
obj.deposit()
print(obj.get_balance())'''
        
#Create two classes, Rectangle and Circle. Both should have a method area().
#Call the area() method from a common interface.
'''class shape():
    def area(self):
        print("Parent class")
class Rectangle(shape):
    def area(self):
        print("Area of the rectangle")

class Circle(shape):
    def area(self):
        print("Area of the circle")
obj=Circle()
obj.area()'''

'''class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year} - Genre: {self.genre}"

# Example Usage
book = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
print(book)  # Output: 'To Kill a Mockingbird' by Harper Lee, published in 1960 - Genre: Fiction
'''
#Create a class Employee with attributes like name, id, and salary.
#Add methods to update salary and display details.
'''class Employee():
    def __init__(self):
        self.name=input("enter the name")
        self.salary=int(input("enter the salary name"))

    def update(self):
        self.new=int(input("input the new salary"))
        self.salary = self.new

    def display(self):
        print(f"Employee name {self.name} and salary {self.salary}")
obj1=Employee()
obj1.display()
obj1.update()
obj1.display()'''


class person():
    def __init__(self):
        self.name=input("enter the namae")
        self.age=int(input("enter the age"))
        self.depart=input("enter the department")
        if(self.depart.lower() =="manager"):
           manager=Manager(self.name,self.age,self.self.depart)
           manager.display()
        if self.depart.lower() == "dev":
            dev=Dev(self.name,self.age,self.self.depart)
            dev.display()
class Manager:
    def __init__(self,name,age,depart):
        self.name=name
        self.age =age
        self.depart =depart
    def display(self):
        print(f"{self.name} from {self.depart} has {self.age}")
class Dev:
    def __init__(self,name,age,depart):
        self.name=name
        self.age =age
        self.depart =depart
    def display(self):
        print(f"{self.name} from {self.depart} has {self.age}")

obj=person()

    

