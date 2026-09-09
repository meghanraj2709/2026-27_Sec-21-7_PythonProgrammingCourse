#To calculate compound interest
principal = float(input("Enter the principal amount in Rupees:"))
rate = float(input("Enter the rate of interest in percentage:"))
time = float(input("Enter the time in years:" ))
amount = principal*(1+rate/100)**(time)
CompoundInterest = amount - principal
print("The required compound interest is:",CompoundInterest)
