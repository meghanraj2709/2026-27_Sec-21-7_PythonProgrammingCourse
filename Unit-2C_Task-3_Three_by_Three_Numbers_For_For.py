#to print numbers in a 3x3 grid using for-for nested loop
num = 1  
for row in range(1, 4):  
    for col in range(1, 4): 
        print(num, end=" ") 
        num = num + 1 
    print()