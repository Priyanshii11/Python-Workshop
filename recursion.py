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
print_numbers(num)

 
