# palindrome
'''x=121
num =x
val =0
while(x>0):
    rem = x%10
    x//=10
    val = val*10 + rem
print(val)
if(val ==num):
    print("Palindrome number")
else:
    print("Not Palindrome number")

#Prime number
for i in range(2,100):
    flag = 0
    for j in range(2,i):
        if(j%i==0):
            flag = 1
            break
if(flag==1):
    print("prime number:" ,num)
else:
   print("not a prime number")

#wap to print 1,2,3,5,6,7,8,9 using continue 
for i in range(1,10):
    if(i==4):
        continue
    print(i,end = " ")

#wap to print number sum of 50 natural number
num=50
sum1 =0
for i in range(1,num+1):
    sum1 = sum1+i
print(sum1,end=" ")'''

#armstrong number
num = 153
a=num
l = len(str(num))
val =0 
while(num >0):
     rem = num%10
     num = num//10
     val = val + rem**l
print(val)
if(a==val):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
     

