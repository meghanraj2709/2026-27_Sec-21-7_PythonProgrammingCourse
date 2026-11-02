#program to print the multiplication table of a number
number = int(input("Enter the multiplication number: "))
for multiplier in range(1,11):
    product = number * multiplier
    print(f" {number} x {multiplier} = {product}")