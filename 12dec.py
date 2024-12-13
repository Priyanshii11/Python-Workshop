#inheritance
#write all ineritance program with init method

#multiple inheirttane
'''
class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method ")
class Mother:
    def __init__(self):
        print("Mother class constructor")
    def showM(self):
        print("Mother class method ")   
class son(Father,Mother):
    def __init__(self):
        print("son class constructor")
    def shows(self):
        print("son class method ")
obj=son()
obj.showF()
obj.shows()
obj.showM()'''


#Hybrid inheritance

#Super Keyword
'''class A:
    def __init__(self):
        print("a")
class B(A):
    def __init__(self):
        print("b")
class C(B):
    def __init__(self):
        print("c")
        super(B,self ).__init__()

obj=C()


class A:
    def __init__(self):
        print("a")
    def display(self):
        print("self A")
class B(A):
    def __init__(self):
        print("b")
    def display(self):
        print("self B")
        super().display()
obj=B()
obj.display()

class square():
    def __init__(self,a):
        self.a=a
    def area(self):
        print("Area of the Rectangle ",(self.a*self.a))
    def peri(self):
        print("Perimeter of the rectangle",(2*self.a))


class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of the Rectangle ",(self.b*self.l))
    def peri(self):
        print("Perimeter of the rectangle",(2*(self.b+self.l)))
obj=Rectangle(3,4)
obj.area()
obj.peri()
obj2=square(6)
obj2.area()
obj2.peri()


class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of the Rectangle ",(self.b*self.l))
    def peri(self):
        print("Perimeter of the rectangle",(2*(self.b+self.l)))
class square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)
    def area(self):
        print("Area of the Rectangle ",(self.a*self.a))
    def peri(self):
        print("Perimeter of the rectangle",(2*self.a))

obj2=square(6,3)
obj3=square(3)
obj3.area()
obj3.peri()'''


#diamond problem resolvment MRo also show class hierarchy
'''class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")
class C(A):
    def __init__(self):
        print("C")
class D(B,C):
    def __init__(self):
        print("D")
d=D()
print(D.__mro__)'''


'''class A:
    def __init__(self):
        print("A")
class B:
    def __init__(self):
        print("B")
class C(A,B):
    def __init__(self):
        print("C")
c=C()
print(C.__mro__)


class A:
    def __init__(self):
        print("A")
class B:
    def __init__(self):
        print("B")
class C(A,B):
    def __init__(self):
        print("C")
class D(C,B):
    def __init__(self):
        print("D")
d=D()
print(D.__mro__)'''



