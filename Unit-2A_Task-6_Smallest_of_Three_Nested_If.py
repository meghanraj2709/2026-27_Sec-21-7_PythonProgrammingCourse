#To find the smallest of three numbers using nested if
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a <= b:
    if a <= c:
        SmallestNumber = a
    else:
        SmallestNumber = c
else:
    if b <= c:
        SmallestNumber = b
    else:
        SmallestNumber = c
print("The smallest number among",a,b,c,"is",SmallestNumber)