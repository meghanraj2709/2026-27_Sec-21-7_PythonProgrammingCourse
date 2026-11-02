#program to find the factorial of a number using for loop
number = int(input("Enter the number: "))
factorial = 1  
for i in range(1, number + 1):  
    factorial = factorial * i  
print(f"Factorial of {number} is {factorial}")