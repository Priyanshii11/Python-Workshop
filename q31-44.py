'31'
'''num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
if(num1==num2):
    print("Same number")
else:
    print("Not Same number")
'32'
num1=int(input("enter the number :"))
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
    print("not valid number")
    
'33'
num=int(input("enter the number : "))
if (num%7==0):
    print("This number is divisible by 7")
else:
    print("this number is not divisible by 7")
print()

'34'
num1 =int(input("enter the number : "))
num2 =int(input("enter the number : "))
num3 =int(input("enter the number : "))
if(num1>num2 and num1>num3):
    print(num1,"is number greatest number")
elif(num2>num1 and num2>num3):
    print(num2,"is number greatest number")
else:
    print(num3,"is the greatest number")

'39'
while True:
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
            print("Invalid number! Please enter a number between 1 and 7.")
            
'38'
word = input("enter the letter :   ")
if word in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")
    
'40'
colors = {
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
    print("No color found with this letter")
    
'36'
st = input("enter the words : ")
print(st.lower())
print(st.upper())

'37'
num = int(input("enter the number : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

'35'
# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
# Nested if to find the greatest number
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

# Output the result
print(f"The greatest number among {num1}, {num2}, and {num3} is {greatest}.")

 '41'
print("Welcome to the Arithmetic Calculator!")
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (^)")

# Input the operation choice
choice = input("Enter the number corresponding to the operation (1-6): ")

# Input two numbers for the calculation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the user's choice
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
    print("Invalid choice! Please select a valid operation.")


'42'
print("1.Area of the Circle")
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
            print("Area of square =",area)

'44'
num =input("enter the digit,char,consonants : ")
if num in ('a','i','e','o','u'):
    print("Vowels")
elif num in ('1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'0' ):
    print("Digits")
else:
    print("Consonants")

'43'
num1 =int(input("Enter the first subject  Marks : "))
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








           
