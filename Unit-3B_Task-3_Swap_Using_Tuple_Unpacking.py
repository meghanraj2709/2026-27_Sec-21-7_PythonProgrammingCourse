#program to swap two variables using tuple unpacking
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print("Before:", first_number, second_number)
first_number, second_number = second_number, first_number
print("After:", first_number, second_number)