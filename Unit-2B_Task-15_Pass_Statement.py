#program to demonstrate use of pass statement using for loop and using while loop
n = int(input("Enter the value of n: "))
counter = 1  
while counter <= n: 
    if counter % 3 == 0:  
        pass  
        print(f"Used pass for multiple of 3: {counter} (N is {n})")  
    else:
        print(f"while loop number = {counter} (up to {n})")
    counter = counter + 1 