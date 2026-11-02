#program to demonstrate use of continue statement using for loop 
n = int(input("Enter N (print 1 to N, skip even numbers): "))
for num in range(1, n + 1): 
    if num % 2 == 0:  
        print(f"Skipping even number {num} with continue (N is {n})")  
        continue
    print(f"for loop odd number = {num} (up to {n})")  