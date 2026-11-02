#to find the largest number in a series of N numbers entered by the user using for loop
total_input_numbers = int(input("Enter how many numbers: "))
largest = float(input("Enter a number: "))
for i in range(total_input_numbers - 1):
    num = float(input("Enter a number: "))  
    if num > largest:  
        largest = num  
print(f"Largest among {total_input_numbers} numbers is {largest}")