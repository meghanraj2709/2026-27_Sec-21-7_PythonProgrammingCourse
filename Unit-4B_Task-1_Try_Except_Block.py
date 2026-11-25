#catches ZeroDivisionError when dividing 10 by 0
try:
    num_1 = int(input("Enter a number as dividend: "))
    num_2 = int(input("Enter a number as divisor: "))
    division = num_1/num_2
    print(f"Division of {num_1} with {num_2} is {division}")
except ZeroDivisionError:
    print(f"Division of {num_1} with {num_2} is not possible.")