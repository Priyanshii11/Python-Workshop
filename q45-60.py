"""
'45'        
for i in range(1,20):
    if(i%2==0):
        print(i , end = " ")
print()

'46'
for i in range(1,100):
    if(i%7==0):
        print(i , end = " ")
print()

"47"
num = int(input("enter the number for table :"))
for i in range(1,11):
    print(num, "*" ,i,"=",(i*num))
"48"    
num = 0
for i in range(1,50+1):
    num += i
print(num, end = " ")

'49i'
num = int(input("enter the number: "))
for i in range(1,num):
    num *= i
print(num, end = " ")

'49ii'
num = int(input("enter the number : "))
factorial = 1
i = 1
while i <= num:
        factorial *= i
        i += 1
print(factorial)

'50'
sum = 0
num = int(input("enter the number : "))
while num >1:
    rem = num % 10
    num = num //10
    sum +=rem
print(sum)

"51"
sum = 0
num = int(input("enter the number : "))
while num >1:
    rem = num % 10
    num = num //10
    sum = sum *10 +rem
print(sum)

"54"
num = int(input("enter the number"))
power = int(input("enter the value"))
value = num**power
print(f"power of {num} to the power of {power} is {value}")

"55"
n = int(input("enter the n value"))
r = int(input("enter the r value"))
num = 1
num2 = 1
for i in range(1,n+1):
    num *= i
for i in range(1,r+1):
    num2 *= i
num3=1
for i in range(1,n-r+1):
    num3 *= i
value = num/(num2*num3)
print("nCr value is ",value)
"57"
sum =0
num = int(input("enter the number : "))
ori=num
while num >1:
    rem = num % 10
    num = num//10
    sum = sum*10+rem
print(sum)
if(sum==ori):
    print("palindrome number")
else:
    print("not a palindrome number")"""

"59"



