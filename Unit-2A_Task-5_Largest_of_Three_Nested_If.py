#To find the largest number of three numbers 
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a >= b:
    if a >= c:
        LargestNumber = a
    else:
        LargestNumber = c
else:
    if b >= c:
        LargestNumber = b
    else:
        LargestNumber = c
print("The Largest number among",a,b,c,"is",LargestNumber)