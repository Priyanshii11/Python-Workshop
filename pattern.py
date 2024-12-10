"""for i in range(5):
    for j in range (i+1):
        print("*",end=" ")
    print()
print() 
for i in range(5):
    for j in range(5):
        print("*" , end =" ")
    print()
print()
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end =" ")
    print()
print()
for i in range(1,6):
    for j in range(1,i+1):
        print(j , end = " ")
    print()
print()
value = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(value) , end = " ")
    print()
    value = value+1
print()
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()
print()
value = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(value) , end = " ")
        value = value+1
    print()
print()

k=1 
for i in range(1,6):
    for j in range(1,k+1):
        if(j%2!=0):
            print("0",end=" ")
        else:
            print("1",end =" ")
    print()
    k=k+2
for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end = " ")
    for k in range(1,i*2):
        if(k !=1 or k==i*2):
            print("*",end = " ")            
        else:
            print("3",end = " ")
    print()"""

rows=6
for i in range(rows):
    print(" " * (rows - i), end=" ")
    value = 1
    for j in range(i + 1):
        print(f"{value} ", end=" ")
        value = value * (i - j) // (j + 1)
    print()  # Move to the next line
