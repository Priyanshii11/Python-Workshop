'''y = lambda x: x**2
print (y(4))

y = lambda x,y : x+y
print (y(4,5))


y = lambda a: "even" if (a %2==0  )  else "odd"
print (y(6))

y = lambda a,b: a if (a > b )  else b
print (y(6,4))


y = lambda a: "Positive" if (a > 0  ) else  "Negative" if(a<0)   else "zero"
print (y(6))
print(y(-9))


y = lambda a : "A" if (a>=90) else "B" if(a>=80) else "C" if(a>=70 ) else "Fail"
print(y(70))
print(y(40))

def sqr(num):
    return num**2
number = [1,2,3,4,5]
y = map(sqr, number)
print(list(y))

lst = ['Ram','Sit a' ,'geeta']
def length(Str):
    return len(Str)
y = map(length,lst)
print (list(y))

lst = ['Ram','Sita' ,'geeta']

y =list(map(lambda Str : len(Str) ,lst))
print(list(y))
def sqr(num):
    return num**2
number = [1,2,3,4,5]
y = map(sqr, number)
val = list(y)
    sum1 = sum1  +i
    
print(sum1)

a= input("enter the number :")
def inte(num):
    return int(num)
print(lst)
y = list(map(inte,lst))
print(y)
input_string = input("Enter numbers separated by commas: ")

string_list = input_string.split(',')

print(string_list)

def change(n):
    return int(n)
x= list(map(change,string_list))
print(x)

lst =[1,3,5,'ram', [1,2,3]]

def DType(item):
    return type(item)
y = map(DType , lst)
print(list(y))'''

lst =[1,2,3,4,5,7]
def DType(item):
    if(item %2==0):
        return item
y = map(DType, lst)
x = i for i in y if i is not None # Exclude None values
print(x)

'''lst = ['Ram','Sita','Mohan','Rashmi']
x=list(filter (lambda x: len(x)>4 , lst))
print(x)

def inLower(x):
    return x.lower()
y=map(inLower ,lst)
print(list(y))

x=10 #global
def outer():
    x=12 #enclosed var
    def inner():
        x=7 #local
        print("inner ",x)
    inner()
    print("Outer ",x)
outer()
print("outsode the function",x)

import  pckg
print(pckg.xyz(5,6))
print(pckg.power(5))
print(pckg.div(5,6))
print(pckg.mul(5,6))

import calendar

# Input the year and month
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
# DiSplay the calendar
print(calendar.month(year,month))

 
from pckg import xyz
print(xyz(3,4))
 
from pckg import xyz as x
print(x(3,4)) 
 
def add(x,y):
    return (x+y)
lst =[1,2,3,4,5]
from functools import reduce
y=reduce(add,lst)
print(y//5)'''







