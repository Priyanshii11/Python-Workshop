#35.Write a program to Accept two Integers and Check if they are Equal
'''a=int(input("enter the number"))
b=int(input("enter the number"))
if(a==b):
    print("numbers are equal")
else:
    print("Numbers are not equal")'''

#36. Write a program to Check if a given Integer is Positive or Negative and Odd or Even. 
'''num1=int(input("enter the number :"))
if num1 > 0:
    print("Positive number")
elif num1 < 0:
    print("Negative number")
else:
    print ("zero number")
if num1%2==0:
    print("Even number")
elif num1%2 != 0:
    print("Odd number")
else:
    print("not valid number")'''

#37.Write a program to Check if a given Integer is Divisible by 7 or not.
'''num=int(input("enter the number : "))
if (num%7==0):
    print("This number is divisible by 7")
else:
    print("this number is not divisible by 7")
print()'''

#38.Write a program to find the greatest of three numbers using else if ladder.
'''num1 =int(input("enter the number : "))
num2 =int(input("enter the number : "))
num3 =int(input("enter the number : "))
if(num1>num2 and num1>num3):
    print(num1,"is number greatest number")
elif(num2>num1 and num2>num3):
    print(num2,"is number greatest number")
else:
    print(num3,"is the greatest number")'''

#39.Write a program to find the greatest of three numbers using Nested if.'''num1 = float(input("Enter the first number: "))
'''num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2:
    if num1 >= num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 >= num3:
        greatest = num2
    else:
        greatest = num3
'''

#40.Write a program to convert an Upper-case character into lower case and vice-versa.
'''st = input("enter the words : ")
print(st.lower())
print(st.upper())'''

#41.Write a program to check weather an entered year is leap year or not.
'''num = int(input("enter the number : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")'''

#42.Write a Program to check whether an alphabet entered by the user is a vowel or a constant.
'''word = input("enter the letter :   ")
if word in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")'''

#43.	Write a program to Read a Coordinate Point and Determine its Quadrant.
# Input the coordinates
'''x = float(input("Enter the X-coordinate: "))
y = float(input("Enter the Y-coordinate: "))
if x > 0 and y > 0:
    print(f"The point ({x}, {y}) lies in Quadrant I.")
elif x < 0 and y > 0:
    print(f"The point ({x}, {y}) lies in Quadrant II.")
elif x < 0 and y < 0:
    print(f"The point ({x}, {y}) lies in Quadrant III.")
elif x > 0 and y < 0:
    print(f"The point ({x}, {y}) lies in Quadrant IV.")
elif x == 0 and y == 0:
    print(f"The point ({x}, {y}) is at the Origin.")
elif x == 0:
    print(f"The point ({x}, {y}) lies on the Y-axis.")
elif y == 0:
    print(f"The point ({x}, {y}) lies on the X-axis.")'''


#44.	Write a program to Add two Complex Numbers.
'''num1=complex(input("Enter the complex number1"))
num2=complex(input("Enter the complex number 2"))
num3 =num1+num2
print(f"Addition of two complex number {num} and {num2} is {num3}")'''

#45.	Write a Program to find roots of a quadratic expression
'''import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check the nature of the discriminant
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"The roots are real and distinct: {root1} and {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The roots are real and equal: {root}")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"The roots are complex: {real_part} + {imaginary_part}j and {real_part} - {imaginary_part}j")

# Input coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    find_roots(a, b, c)
'''

#46.Write a program to print day according to the day number entered by the user.
'''while True:
    num = int(input("Enter a number (1-7, or 0 to exit): "))
    
    if num == 0:  # Exit condition
        print("Exiting the program.")
        break
    
    match num:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid number! Please enter a number between 1 and 7.")'''



#47.Write a program to print color name, if user enters the first letter of the color name.
'''colors = {
    'r': 'Red',
    'g': 'Green',
    'b': 'Blue',
    'y': 'Yellow',
    'o': 'Orange',
    'p': 'Purple',
    'w': 'White',
    'k': 'Black'
}
word =input("Enter the color name : ").lower()
if word in colors:
    print(f"The name of this color is {colors[word]}.")
else:
    print("No color found with this letter")'''

#48. Write a program to Simulate Arithmetic Calculator.
'''print("Welcome to the Arithmetic Calculator!")
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (^)")
choice = input("Enter the number corresponding to the operation (1-6): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if choice == '1':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}.")
elif choice == '2':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}.")
elif choice == '3':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}.")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}.")
    else:
        print("Division by zero is not allowed.")
elif choice == '5':
    result = num1 % num2
    print(f"The result of {num1} % {num2} is {result}.")
elif choice == '6':
    result = num1 ** num2
    print(f"The result of {num1} ^ {num2} is {result}.")
else:
    print("Invalid choice! Please select a valid operation.")'''


#49.Write a menu driven program for calculating area of different geometrical
#figures such as circle, square, rectangle, and triangle.
'''print("1.Area of the Circle")
print("2.Area of the Square")
print("3.Area of the Rectangle")
print("4.Area of the Triangle")
while True:
    choice = int(input("enter the choice (1-4) , or exit press 0 : "))
    if choice==0:
        print ("Exiting the program ")
        break
    match choice:
        case 1:
            print("Area of Cirlce")
            num = int(input("enter the radius : "))
            area = 3.14*num*num
            print("Area of cirrcle =",area)
        case 2:
            print("Area of Square")
            num =int(input("Enter the length: "))
            area = num*num
            print("Area of square = ",area)
        case 3:
            print("Area of Rectangle")
            num =int(input("Enter the length: "))
            num2 =int(input("Enter the breadth: "))
            area = (num*num2)
            print("Area of square =",area)            
        case 4:
            print("Area of Triangle")
            num =int(input("Enter the length: "))
            num =int(input("Enter the breadth: "))
            area =  (num*num2)/2
            print("Area of square =",area)'''

#50.WAP that accepts the marks of 5 subjects and finds the percentage marks obtained by the student. It also prints grades according to the following criteria: Between 90-100% Print 'A', 80-90%  Print 'B', 60-80%
#Print 'C', 50-60%  Print 'D', 40-50%  Print 'E', Below 40% Print 'F’
'''num1 =int(input("Enter the first subject  Marks : "))
num2 =int(input("Enter the second subject Marks : "))
num3 =int(input("Enter the third subject  Marks : "))
num4 =int(input("Enter the fourth subject  Marks : "))
num5 =int(input("Enter the fifth subject  Marks : "))
total =(num1+num2+num3+num4+num5)/5
print(total,"Avg Marks")
if(total >=90):
    print("A")
elif(total >=80 and total <90):
    print("B")
elif(total >=60 and total <80):
    print("C")
elif(total >=50 and total <60):
    print("D")
elif(total >=40 and total <50):
    print("E")
else:
    print("F")'''
#51 WAP to enter a character and then determine whether it is a vowel, consonants, or a digit.
'''num =input("enter the digit,char,consonants : ")
if num in ('a','i','e','o','u'):
    print("Vowels")
elif num in ('1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'0' ):
    print("Digits")
else:
    print("Consonants")'''
