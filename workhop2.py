'''num1 =int(input("Enter the first subject  Marks : "))
num2 =int(input("Enter the second subject Marks : "))
num3 =int(input("Enter the third subject  Marks : "))
num4 =int(input("Enter the fourth subject  Marks : "))
num5 =int(input("Enter the fifth subject  Marks : "))
num6=(num1+num2+num3+num4+num5)/500
total=num6*100
print(total,"Percentage")
if(total >=90):
    print("First")
elif(total >=80 ):
    print("second")
elif(total >=70 ):
    print("Third")
else:
    print("Fail")
'''
'''
num1 =int(input("Enter the first number: "))
num2 =int(input("Enter the second number : "))
num3 =int(input("Enter the third number : "))
if(num1>num2):
    if(num1>num3):
        print(num1,"greatest among all three")
    else:
        print(num3 ,"greatest among all three")
else:
    if(num2>num3):
        print(num2, "greater than among three:")
    else:
        print(num3,"greater than all three")

num =int(input("enter the number: "))       
for i in range(1,11):
        print(num ," *  " ,i," = ", i*num)

for i in range(1,51):
    if(i%2==0):
        print(i , end="  ")
s=0
for i in range(0,11):
    s=s+i
print("sum of 1-10 is ",s , end=" ")

num =int(input("enter the number: "))       
s=1
for i in range(1,num+1):
    s=s*i
print("factorial is ",s , end=" ")
s=0
lst = [5,6,7,8]
for i in lst:
    s =i+s
print(s)

lst = [1,3.5,'sam' ,[1,2,3]]
for i in lst:
    print(type(i))

lst = ['sam','gupta','hari']
for i in lst:
    print(len(i))
    

lst = "santosh"
for i in lst:
    if  i in ('aeiouAEIOU'):
        print (i, end=" ")

lst2=[]
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if(i%2==0):
        lst2.append(i)
print(lst2)

sum1 = 0
st='santosh'.upper()
for i in st:
    sum1 = sum1 + ord(i)
print(sum1)

num = 1
while(num <=10):
    print(num)
    num=num+1
    
num = 10
while(num >=1):
    print(num)
    num=num-1

num = 0
i=0
while (i<=5):
     num = num+i
     i=i+1
     print(num)
num = 1
i=5
while (i>=1):
     num = num*i
     i=i-1
print(num)

num = 321
val =0
while(num>0):
    rem = num%10
    num = num//10
    val = rem+val
print(val)

num = int(input("enter the number "))
while(num>0):
    s = num%2
    num = num//2
    print(s , end=" ")


s=0
num = int(input("enter the number "))
while(num>0):
    rem = num%10
     num = num//10
     s = s*10+rem
print(num2 , end=" ")

a=121
su=a
val =0
while(a>0):
    rem = a%10
    a=a//10
    val =val*10+rem
if(val==su ):
    print("palindrome number")
else:
    print("not a palindrome")

for i in range(1,6):
    for j in range(1,6):
        print("*" ,end=" ")
    print()
     
a=64
for i in range(1,6):
    for j in range(1,6):
        print(chr(a+j),end=" ")
    print()
a=64
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(i+a) ,end=" ")
    print() 
for i in range(1,6):
    for j in range(1,6-i+1):
        print("*",end=" ")
    print()

a= 0
for i in range(1,6):
    for j in range(1,6-i+1):
        print(a+j,end=" ")
    print()

a= 64
for i in range(1,6):
    for j in range(1,6-i+1):
        print(chr(a+j),end=" ")
    print()

for i in range(1,6):
    for j in range(1,6-i+1):
        print(" " , end = " ")
    for j in range (1,i+1):
        print("*" , end = " ")
    print()


for i in range(1,6):
    for j in range(1,6-i+1):
        print(" " , end = " ")
    for j in range (1,2*i):
        print("*" , end = " ")
    print()
a=0
for i in range(1,6):
    for j in range(1,6-i+1):
        print( " ", end = " ")
    for j in range(1,i):
        print (a+i , end = " ")
    print()
a=1
for i in range(1,6):
    for j in range(1,i+1):
        print(a,end="  ")
        a=a+1
    print()
a=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(a),end="  ")
        a=a+1
    print()
i = 0
a,b = 0,1
num = int(input("enter the number ")) 
while(i<num):
    print(a, end = " ")
    a,b = b , a+b
    i=i+1
print()'''

sum2=0
num =int(input("enter the value of n "))
l=len(str(num))
while(num>0):
    s = num%10
    num = num//10
    sum2 = sum2+s**l  
print(sum2)

'''for i in range(1,6):
     for j in range(1,6-i+1):  
        print(" " , end = " ")
    for j in range (1,2*i):
        print("*" , end = " ")
    print()
for i in range(5,0 ,-1):
    for j in range(1,6-i+1):
        print(" " , end = " ")
    for j in range (1,2*i):
        print("*" , end = " ")
    print()
    
a=64
for i in range(1,6):
    for j in range(1,6-i+1):
        print("  " , end = "  ")
    for j in range (1,2*i):
        print(chr(64+j) , end = "  ")
    print()'

for i in range(1,6):
    for j in range(1,6-i+1):
        print("  " , end ="  ")
    for j in range (1,2*i):
        print(chr(64+j) , end = "  ")
    for j in range(1,j+1):
        print(chr(64) , end =" ")
    print()

bi = []
num = 6
while(num >0):
    a = num % 2
    num =num//2
    bi.append(a)
for i in reversed(bi):
    print(i,end = " ")

num = 1101
a=0
for i in range(num):
    a = 2**i + a
    print(a ,end = " " )'''
    
