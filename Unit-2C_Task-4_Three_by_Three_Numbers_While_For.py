# to print numbers in a 3x3 grid using while-for nested loop
num = 1 
row_loop_var = 1 
while row_loop_var <= 3:
    for col in range(1, 4):  
        print(num, end=" ") 
        num = num + 1
    print() 
    row_loop_var = row_loop_var + 1 