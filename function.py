#102 Write a Python function to sum all the numbers in a list.  
'''def add(num):
    sum1=0
    for i in range (len(lst)):
        sum1 = sum1+lst[i]
    return sum1
lst=[8,2,0,3,7]
x=add(lst)
print(x)
'''
#103 Write a Python function to multiply all the numbers in a list.  
'''def mul(num):
    sum1=1
    for i in range (0,len(lst)):
        sum1 = sum1*lst[i]
    return sum1
lst=[8,2,-1,3,7]
x=mul(lst)
print(x)'''

#104 Write a Python program to reverse a string.  
'''def reverse(Str):
    return Str[ : :-1]
Str="1234abcd" 
x=reverse(Str)
print(x)'''

#105 Write a Python program calculate the factorial of a number using lambda and reduce functions.
#The function accepts the number as an argument. 
'''fac=1
y = lambda x: fac for i in range(1,x) fac =fac*i
print(y(2))'''

#106 Write a Python function to check whether a number falls in a given range.  
'''def range1(num,a,b):
    if num in range(a,b):
        return "Number falls in range"
    else:
        return "Number did nt fall in range"
a=int(input("enter the starting range"))
b=int(input("enter the ending range"))
num=int(input("Enter the number "))
x=range1(num,a,b)
print(x)'''

#107  Write a Python function that accepts a string and
#calculate the number of upper-case letters and lower-case letters.  
'''Str = "The quick Brown Fox"
def String(Str):
    upper_case =0
    lower_case =0
    for i in Str:
        if i.isupper():
            upper_case = upper_case+1
        elif i.islower():
            lower_case+=1
    print("No. of upper case character are =",upper_case)
    print("No. of lower case character are =",lower_case)
String(Str)'''

#108 Write a Python function that takes a list and#
#returns a new list with unique elements of the first list.  
'''lst =[1,2,3,3,3,3,4,5]
def dislist(lst):
    lst2=[]
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    print(lst2)
dislist(lst)'''


#109. Write a Python function that takes  a number as a parameter and check the number is prime or not.
'''def Prime(num):
    for i in range(2,num):
        flag =0
        for j in range(2,i):
            if(j%i==0):
                flag = 1
                break
    if(flag==0):
        print("It is Prime number")
    else:
        print("It is not a Prime number")

a = int(input("Enter the number to check that number is prime or not :"))
Prime(a)'''

#110. Write a Python function that checks whether a passed string is palindrome or not.


#111. Write a Python function that prints out the first n rows of Pascal's triangle.

#112. Write a Python function to check whether a string is a pangram or not.
'''a = input("Enter a sentence: ")
alphabet = set("abcdefghijklmnopqrstuvwxyz")  
sentence_letters = set(a.lower())  
if alphabet.issubset(sentence_letters):
    print("Pangram")
else:
    print("Not a Pangram")'''


#113. Write a Python function that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
#Sample Items: green-red-yellow-black-white
'''def sort(sequence):
    words = sequence.split('-')
    words.sort()
    sorted_sequence = '-'.join(words)
    print(sorted_sequence)

input_s= "green-red-yellow-black-white"
sort(input_s)'''


#114 Python function to convert height (in feet and inches) to centimeters. 
'''def convert(num1,num2):
    inches =num1*12
    centi =inches*2.54+num2*2.54
    return centi
print(convert(5,4))'''



#115 Python function to Convert Celsius to Fahrenheit.
'''def convert(cel):
    num = (cel*9/5)+32
    return num
a =int(input("enter the number"))
x=convert(a)
print(x)'''

#116.Python function to display all the Armstrong number from 1 to n.

'''def Armstrong(num):
    val=0
    num2 =num
    l=len(str(num))
    while(num>0):
        rem=num%10
        num //=10
        val = val + rem**l
    if(val==num2):
        print("Armstrong Number as both are sam ",val)
    else:
        print("Not Armstrong number as both are different ",val,"and" ,num2)
a=int(input("Enter the number"))
Armstrong(a)'''

