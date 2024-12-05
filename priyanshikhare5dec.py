
# print the pattern
'''A
B A B
A  B A B A
B  A B A B A B'''

'''rows = 4  
for i in range(1, rows + 1):
    for j in range(1, 2 * i):
        if j % 2 == 0:
            print("B", end=" ")
        else:
            print("A", end=" ")
    print()'''

#wap to find the sum of number 1 to n using recursion
"""def sum1(num):
    if(num == 0):
        return 0
    else:
        return num+sum1(num-1)
y=int(input("enter the number : "))
print(sum1(y))"""

#wap to find the sum of all the prime num from 1, 1000
'''def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    sum1 = 0
    for num in range(2, limit + 1):  
        if is_prime(num):
            sum1 += num
    return sum1

limit =1000
result = sum_of_primes(limit)
print(f"The sum of all prime numbers up to {limit} is {result}.")'''

#fibonacci series using function
'''def fibo(num):
    i = 0
    a,b = 0,1
    while(i<num):
        print(a, end = " ")
        a,b = b , a+b
        i=i+1
print()
fibo(5)'''

#write a function that acccept a string and calculate the number of upper case letter and lower case letter
#string ="The Quick Brown Foxs"

'''Str = "The Quick Brown Foxs:"
cap =0
smll = 0
for i in Str:
    if  (ord(i) >=65 and ord(i)<90):
        cap = cap+1
    elif (ord(i) >=97 and ord(i)<122):
        smll =smll+1
print("Capital value is " , cap , "and Small letter is " ,smll )'''
