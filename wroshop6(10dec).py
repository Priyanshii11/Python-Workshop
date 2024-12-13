#closure and decorator Advanced python concepts
'''def name():
    return 'Santosh'
def outer(funct):
    def inner():
        x=funct()
        return x +'Hi'
    return inner
y=outer(name)
print(y() )'''


'''def outer(funct):
    def inner():
        x=funct()
        print("Hi" ,x)
    return inner
@outer 
def name():
    return 'Priyanshi '
y=name()'''

#most important
'''def outer(funct):
    def inner(t,p):
        x=funct(t,p)
        for i in range(1,5):
            print(p ,end=" " )
        print()
        print(x.upper())
        for i in range(1,5):
            print(p ,end=" " )
    return inner
@outer
def name(text,p):
    return text
y=name('santosh','#')'''
'''#decotaer number 1
def upper(funct):
    def inner():
        x=funct()
        return x.upper()
    return inner
#decorater number 2
def listOuter(func):
    def listinner():
        x=func()
        return list(x)
    return listinner
@listOuter 
@upper 
def name():
    lst = input("enter name:")
    return lst
y=name()
print(y)'''

#decotaer number 1
'''def upper(funct):
    def inner(t):
        x=funct(t)
        return x.upper()
    return inner
#decorater number 2
def listOuter(func):
    def listinner(t):
        x=func(t)
        return list(x)
    return listinner
@listOuter 
@upper

def name(t):
    return t

lst = input("enter name:")
y=name(lst)
print(y)
'''
#class and onject or oops concept
'''class myclass:
    cn = "niet:"
    def read(van):
         return"hello"
    def write(ban):
         return 'niet'
obj =myclass()
print(type(obj))
obj2 =myclass()
print(obj.cn)
print(obj.read())
print(obj.write())'''


'''class abc:
  x=20
  def xyz(self):
      return "hello"
p1=abc()
print(p1.xyz())
print(abc().xyz())'''

'''class abc:
    print("hello")
    def __init__(self,name,age):
        self.name=name
        self.age =age
a=input("Enter the name")
b=int(input("Age"))
p1=abc(a,b)
print(p1.name)
print(p1.age)'''

'''class abc():
    def __init__(self):
        self.name=input("enter the name:")
        self.age =int(input("age"))
    def intro(self):
        print (f" my name is {self.name} and my age is {self.age}")
p1=abc()
p1.intro()'''

#wap tht has a class circle used a class varaible to define the value of constant pi=3.14
#use this class variable to calculate area and circumference of a circle with specific radius

'''class Circle():
    p =3.14
    def __init__(self):
        self.r=int(input("enter the radius:"))
    def Display(self):
        circ =2*Circle.p*self.r
        print("Circumference of cirle is ",circ)
        area=self.p*self.r*self.r
        print("area of circle is " ,area)
p1=Circle()
p1.Display()'''

#create a bank account then print(Account createdd") and deposit - amount and store in net balance print net balance and withdraw amount insert
#and check comdtion if net>ammont then minus or else print insfficient balance and lastly print (net balance to print)
'''class Bank:
    def __init__(self):
        self.blnce = 0  # Initialize balance as an instance variable
        print("Account created")

    def deposit(self):
        amount = int(input("Enter the amount you want to deposit: "))
        self.blnce += amount  
        print("Total amount stored in your bank account after deposition:", self.blnce)

    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if self.blnce >= amount:
            self.blnce -= amount  
            print("Total value after withdrawal of money:", self.blnce)
        else:
            print("Insufficient balance")

    def display(self):
        print("Total bank balance is:", self.blnce)

b = Bank()
while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        b.deposit()
    elif choice == 2:
        b.withdraw()
    elif choice == 3:
        b.display()
    elif choice == 4:
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")'''


#write a claas that accpet a string and stores
#details such as number of uppercase character lower character vowel and consonants space and nunber
'''class String:
    def __init__(self):
        self.val = input("Enter the string: ")
        self.lower = 0
        self.upper = 0
        self.vowel = 0
        self.spa = 0
        self.con = 0
        self.digit = 0

    def count(self):
        for i in self.val:  
            if i.isupper():  
                self.upper += 1
            if i.islower():  
                self.lower += 1
            if i in "AEIOUaeiou":
                self.vowel += 1
            elif i.isalpha() and char not in "AEIOUaeiou":  
                self.con += 1
            if i.isdigit():  
                self.digit += 1
            if i.isspace():  
                self.spa += 1

    def display(self):
        print("Uppercase letters:", self.upper)
        print("Lowercase letters:", self.lower)
        print("Vowels:", self.vowel)
        print("Consonants:", self.con)
        print("Spaces:", self.spa)
        print("Digits:", self.digit)


b = String()
b.count()
b.display()'''

                
#wap to display the comment part also in shell     
'''def PQR(x): now i am in class mca and i am too busy in movie
    return "Hello"
print(PQR(2))
print(PQR.__doc__)
        '''
#wap that usses class to store name and marks of the student use list to store the marks in three subject
'''class Student:
    def __init__(self):
        self.name = input("Enter the student's name: ")
        self.marks = []
        print("Enter marks for three subjects:")
        for i in range(3):
            mark = int(input(f"Subject {i + 1}: "))
            self.marks.append(mark)
    
    def display(self):
        print(f"Student Name: {self.name}")
        print("Marks in three subjects:", self.marks)
student = Student()
student.display()'''


#class of polygon then enter length and breadth and find area of rectangle and area of square and permietr fof rectangle and perimetr of square
'''class Polygon():
    def __init__(a):
        a.length= int(input("Enter the string: "))
        a.breadth= int(input("Enter the string: "))
        if(a.length==a.breadth):
            a.square()
        else:
            a.rec()

    def square(a):
        area=a.length*a.breadth
        print("Area of a Square :",area)
        peri=4*a.breadth
        print("Area of a Square :",peri)
    def rec(a):
        area=a.length*a.breadth
        print("Area of a rectangle :",area)
        peri=2* (a.length+a.breadth)
        print("Area of  a perimeter :",peri)
b=Polygon()'''

    
#wap with the class employee that keeps a track of the number of the employee in an org. also stores their name , desognation and salary
'''class Employee:
    # Class variable to keep track of the number of employees
    total_employees = 0

    def __init__(self, name, designation, salary):
        self.name = name  # Store the employee's name
        self.designation = designation  # Store the employee's designation
        self.salary = salary  # Store the employee's salary
        Employee.total_employees += 1  # Increment the total number of employees

    def display_details(self):
        # Display details of the employee
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")
    
    @classmethod
    def get_total_employees(cls):
        # Class method to return the total number of employees
        return cls.total_employees

# Adding employee details
employee1 = Employee("Alice", "Software Engineer", 70000)
employee2 = Employee("Bob", "Project Manager", 120000)
employee3 = Employee("Charlie", "Designer", 60000)

# Display employee details
print("Employee 1 Details:")
employee1.display_details()

print("\nEmployee 2 Details:")
employee2.display_details()

print("\nEmployee 3 Details:")
employee3.display_details()

# Display total number of employees
print(f"\nTotal Employees in the Organization: {Employee.get_total_employees()}")

'''

#Create a class Car with attributes make, model, and year.
#Write a method display() to print the details of the car. Create an object and call the display() method.
'''class Car():
    def __init__(self):
        self.make =input("Enter Company") 
        self.model =input("Write Model name")
        self.year =input("Write Model year")
        
    def display(self):
        print("Company ",self.make)
        print("NAME OF THE CAR ",self.model)
        print("Year of MAking the car ",self.year)
b=Car()
b.display()'''

#worshop7(11dec)
'''class mca:
    cn="niet"
    def __init__(self,x):
        self.x=x
    def display(self):
        print(self.x)
    @classmethod
    def classmethod(cls):
        print(cls.cn)
    @staticmethod
    def fc(n):
        f=1
        for i in range(1,n+1):
            f=f*i
        print(f)
b=mca("priyu")
b.display()
b.classmethod()
b.fc(5)'''

'''class fruit():
    a=0
    def __init__(self,x):
        fruit.num1 =x
        fruit.a=fruit.a+self.num1
    
obj=fruit(3)
obj2=fruit(4)
print(fruit.a)'''

'''class number():
    e=[]
    o=[]
    def __init__(self,x):
        self.num1=x
        if(self.num1%2==0):
            number.e.append(self.num1)
        else:
            number.o.append(self.num1)
obj=number(2)
ob2=number(4)
obj3=number(5)
obj5=number(7)
print(number.e)
print(number.o)'''

#encapsulattion
'''class customer():
    def __init__(self):
        self.__max=900 #private specifier
    def sell(self):
        print("Selling item {}".format(self.__max))
    def setMax(self,price):
        self.__max =price
c=customer()
c.sell()
c.setMax(90000)
c.sell()
c.max=1000
c.sell()'''

#magic method
'''class example():
    def __init__(self,x):
        self.x=x
    def __add__(self,oth):
        print(self.x+oth.x)
    def __mul__(self,oth):
        print(self.x*oth.x)
    def __sub__(self,oth):
        print(self.x-oth.x)
    def __floordiv__(self,oth):
        print(self.x//oth.x)

n=example(4)
n1=example(5)
n*n1
n+n1
n-n1
n//n1'''

'''class distance():
    ft=0
    inc=0
    def __init__(self,x,y):
        self.i =y
        self.f=x
        distance.ft+=self.f
        distance.inc+=self.i
        if(distance.inc>12):
            x=distance.inc-12
            distance.inc=x
            distance.ft +=1 
          
obj=distance(9,5)
obj2=distance(10,9)
print(distance.ft)
print(distance.inc)'''


'''class xyz():
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return "value of x is {}".format(self.x)
obj1=xyz(3)
print(obj1)'''



'''class employe():
    def __new__(cls):
        print("__new__magic method is called")
        inst=object.__new__(cls)
        return inst
    def __init__(self):
        print("__init__ magic method is called")
        self.name='python'
b=employe()
print(b)'''

'''class distance():
    def __init__(self,x,y):
        self.i =y
        self.f=x
    def __add__(self,oth):
        temft=self.f+oth.f
        temin=self.i+oth.i
        if(temin>=12):
            r=temin%12
            q=temin//12
            temft=temft+q
            temin=r
            return distance(temft,temin)
    def __str__ (self):
        return "ft{} in{}".format(self.f,self.i)
obj=distance(9,5)
obj2=distance(10,9)
d3=obj+obj2
print(d3)'''


'''class Complex():
    def __init__(self,x,y):
        self.num =x
        self.im=y
    def __add__(self,oth):
        temnum=self.num+oth.num
        temim=self.im+oth.im
        return Complex(temnum,temim)
    def __str__ (self):
        return "natural number={} imaginary ={}i".format(self.num,self.im)
obj=Complex(9,5)
obj2=Complex(10,9)
d3=obj+obj2
print(d3)'''

##check time
'''class Time():
    def __init__(self,x,y):
        self.min=y
        self.sec=y
    def __add__(self,oth):
        temmin=self.min+oth.min
        temsec=self.sec+oth.sec
        if(temsec>=60):
            r=temsec%60
            q=temsec//60
            temmin=temmin+q
            temsec=r
            return Time(temmin,temsec)
    def __str__ (self):
        return "min {} sec {}".format(self.min,self.sec)
obj=Time(5,55)
obj2=Time(10,45)
d3=obj+obj2
print(d3)'''

#find which one is greaterr
'''class distance():
    def _init_(self,x,y):
        self.x=x
        self.y=y
    def _ge_(self,oth):
        g1=self.x+oth.y/12
        g2=self.x+oth.y/12
        if(g1>g2):
            return True
        else:
            return False

d1=distance(10,5)#self
d2=distance(15,9)#other
d3=d1>=d2
print(d3)'''

'''#inheritence
class father:
    money=1000
    def show(self):
        print("Father class")
    @classmethod
    def showmoney(cls):
        print("Money show",cls.money)
    @staticmethod
    def stat():
        a=10
        print("Static method",a)
class son(father):
    def display(self):
        print("Child class inheritance")
a=son()
a.display()
a.show()
a.showmoney()
a.stat()'''

#constructor overriding
'''class person:
    def __init__(self):
        self.name='santosh'
        print(self.name)
class student(person): 
    def __init__(self):
        print("hi")
S=student()'''




'''class person:
    def __init__(self):
        self.name='santosh'
        print(self.name)
class student(person):
    def display(self):
        print("hi")
S=student()


class person:
    def __init__(self):
        self.name='santosh'
        print(self.name)
    def display(self):
        print("hello")
class student(person):
    def display(self):
        print("hi")
s=student()
s.display()'''


class father():
    def __init__(self):
        self.money=2000
        print("father clss constructor")
class son():
    def __init__(self):
        self.money =5000
        print("son class constructor")
    def display(self):
        print(self.money)
s=son()
    
