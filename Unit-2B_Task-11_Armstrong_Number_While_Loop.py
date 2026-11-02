#To check armstrong number
num = int(input("Enter the 3-digit number: "))
originalnum = num
total = 0
while num > 0:
    digit = num % 10
    total = total + digit ** 3
    num = num // 10
if total == originalnum:
    print(f"{originalnum} is an Armstrong number.")
else:
    print(f"{originalnum} is not an Armstrong number.")