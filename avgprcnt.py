x = int(input("Enter the marks for the first subject: "))
y = int(input("Enter the marks for the second subject: "))
z = int(input("Enter the marks for the third subject: "))
a = int(input("Enter the marks for the fourth subject: "))
b = int(input("Enter the marks for the fifth subject: "))

# Calculate total marks and percentage
sum_marks = x + y + z + a + b
prcnt = (sum_marks / 500) * 100

# Print results
print("Percentage is", prcnt, "and total marks is", sum_marks)
