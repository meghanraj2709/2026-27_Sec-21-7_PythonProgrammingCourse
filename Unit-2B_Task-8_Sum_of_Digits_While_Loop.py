# to find sum of digits of a number using while 
number = int(input("Enter the number: "))
original_num = number
work = number
total = 0
while work > 0:
    digit = work % 10
    total = total + digit
    work = work // 10
print(f"Sum of digits of {original_num} is {total}")