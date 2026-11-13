#program that defines a function to calculate simple interest with parameters principal, time, and rate 
def simple_interest(principal,time,rate = 5):
    SimpleInterest = principal * time * rate / 100
    return SimpleInterest
principal = int(input("Enter the principal amount: "))
time = int(input("Enter the time in years: "))
SimpleInterest = simple_interest(principal,time)
print("SI (default rate):",SimpleInterest)
print("SI (rate=8):",simple_interest(principal,time,8))