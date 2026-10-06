#program to check whether a given number is prime a prime number
number =int(input("Enter the number:"))
if number > 1:
    if number % 2 == 0:
        print(number,"is not a prime number")
    else:
        print(number,"is a prime number")
else:
    print(number,"is not a prime number")