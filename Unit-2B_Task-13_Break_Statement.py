#using break statement
n = int(input("Enter N (print until N, stop early at 5): "))
for i in range(1,n):  
    if i == 6:  
        print(f"Breaking for loop at number 5 (N was {n})")  
        break
print(f"for loop number = 5 (up to {n})")  