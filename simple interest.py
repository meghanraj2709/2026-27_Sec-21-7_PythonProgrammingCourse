#To calculate simple interest
principal = float(input("Enter the principal amount in Rupees: "))
rate = float(input("Enter the rate of interest in percentage: "))
time = float(input("Enter the time in years: "))
SimpleInterest = (principal * rate * time / 100)
print("The required simple interest is:", SimpleInterest)
