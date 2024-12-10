#recursion question
#sum of n number
'''def sum1(num):
    if(num == 0):
        return 0
    else:
        return num+sum1(num-1)
y=sum1(6)
print(y)

#table
def table(num,i=1):
    if(i>10):
        return
    print(f"{num} x {i} = {num * i}")
    table(num ,i+1)
a=7
table(a)

def print_numbers(num):
    if(num ==0):
        return 
    print_numbers(num-1)
    print(num)
num = int(input("Enter a number: "))
print(f"Numbers from 1 to {num}:")
print_numbers(num)'''


'''def fac(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return n*fac(n-1)
y=fac(5)
print(y)

def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
num=int(input())
for i in range(num):
    y=fibo(i)
    print(y ,end=" ")'''

#129.	WAP to convert a list of string type numbers into list of integer type numbers using map function.
#Ex: Input: [‘45’,’88’,’9’]    Output:[45,88,9]
'''lst= [45,88,9]
def change(n):
    return int(n)
y=list(map(change,lst))
print(y)'''

#131.	WAP to compute the cube of all numbers in the given list using map() function.
'''lst =[1,2,3,4,5,6]
def cube(n):
    return n**3
y=list(map(cube,lst))
print(y)'''

#132.	WAP to multiply two numbers using lambda function.
'''y=lambda x,y :x*y
print(y(4,5))'''

#133.	WAP to create a new list consisting of odd numbers from the given list of numbers using filter() function.
'''lst =[1,2,3,4,5,6,7,8,9]
odd_number = list(filter(lambda x: x % 2 != 0, lst))
print(odd_number)'''

#134.	WAP to compute the sum of all the elements of the list using reduce() function.
'''from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,0]
total = reduce(lambda x,y : x+y,numbers)
print(total)'''

#wap to compute posotive integer from list  
'''lst =[1,2,3,-4,4,5]
def change(n):
    if(int(n)>0):
        return int(n)
x=list(filter(change,lst))
print(x)

