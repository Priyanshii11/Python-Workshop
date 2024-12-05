'''for i in range(1,10):
    if(i==5):
        break
    print(i , end = " ")
print("hello")

num =1
while(num <10):
    if(num==5):
        break
    print(num ,end = " " )
    num = num+1
print("hello")

num = int(input("enter the number : "))
i=2
f=0
while(i<num):
    if(num%i == 0 ):
        f=1
        break
    i = i+1
if(f==1):
    print(" Not Prime number")
else:
        print("Prime number")

num = int(input("enter the number : "))
i = 2
while i < num:
    if num % i == 0:
        print("Not a Prime number")
        break
    i += 1
else:
    print("Prime number")

for i in range (1,10):
    if(i==3 or i==7):
        continue
    print(i)
a=51
if(a>100):
    pass
else:
    print("hello")
sum1=0
num = 10011
lst = list(num)
for i in  range(:
    val = 2**i +sum1
print(val)

binary = input("Enter a binary number: ")
decimal = 0

for i in range(len(binary)):
    digit = int(binary[-(i + 1)])  
    decimal =decimal  +  digit * (2 ** i)

print(f"The decimal equivalent of {binary} is {decimal}.")

def sum2(num1,num2):
    print(f"sum of two number :",num1+num2)
sum2(3,4)''

def xyz(name,age=18):
    print("name: ",name)
    print("age: ",age)
xyz('Ram',23)
xyz(age =20,name='Ram')
xyz('priyanshi')

def xyz(*a):
    s=0
    for i in a:
        s=s+i
    print(s)
xyz(2,3)
xyz(7,5,3)

def fact(num):
    s=1
    for i in range(1,num+1):
        s=s*i
    print("factorial = ",s)
fact(5)

def fact(num):
    s=1
    for i in range(1,num+1):
        s=s*i
        print("factorial of " ,i ,"is",s)
fact(10)

def fac(a,b):
    fac = 1
    bfac =1
    dfac = 1  
    for i in range(1,a+1):
        fac=fac*i
    for i in range (1,b+1):
        bfac =bfac*i
    for i in range (1,a-b+1):
        dfac =dfac*i
    ncr = fac/(dfac*bfac)
    return ncr
y =fac(5,2)
print("NCR : " ,y)

def prime(n):
    i=2
    f=0
    while(i<n):
        if(n%i == 0 ):
            f=1
            break
        i = i+1
        if(f==0):
            return n        
for i in range(1,101):
    y= prime(i)
    if(y!=None):
        print(y,end = " " )

 


def Prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1
    else:
        return n
for i in range(1,101):
    y = Prime(i)
    if(y!=None):
        print(y ,end = " " )   


def Anum(num):
    length = len(str(num))
    n = num
    add =0
    while (n>0):
        d = n%10
        add = add+ pow(d,length)
        n//=10
    if(add==num):
        return num
    return None

for i in range(1,200):
    val = Anum(i)
    if(Anum(i) !=None):
        print(val, end = " ")

def name():
    return 'santosh'
def outer(fun):
    def inner ():
        x=fun()
        print('hi',x)
    return inner() 
y=outer(name)

#Recursion
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:  
        return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is {factorial(num)}.")

def fibo(num):
    i=1
    while(i<num):
        a,b = 0,1
        print(a, end = " ")
        a,b = b , a+b
        i=i+1

num = int(input("enter the number "))
print(f"The fibonacci series of {num} is {fibo(num)}.")


def fibo_recursive(n):
    if n <= 1:  
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2) 

num = int(input("Enter the number of terms: "))
print(f"The Fibonacci series of {num} terms is:")
for i in range(num):
    print(fibo_recursive(i), end=" ")

def power(num ,p): 
    if(p == 0):
        return 1
     return num * power(num, p - 1) 
print(power(4,2))


def reverse(s):
    if len(s) ==0 :
        return '  '
    return s[-1] +reverse(s[  :-1])
string ="priyu"
print(reverse(string))

def reverse(s):
    if len(s) ==0 :
        return '  '
    return s[-1] +reverse(s[  :-1])
string ="123"
print(reverse(string))'''
  
def reverse(s):
    if len(s) == 0: 
        return ' '
    return reverse(s[1:]) + s[0]
string = "priyu"
print(reverse(string))   
















