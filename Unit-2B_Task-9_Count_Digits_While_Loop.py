#To count the digits usong while loop
num = int(input("Enter the number: "))
originalnumber = num
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        count = count + 1
        num = num // 10
print(f"Number of digits in {originalnumber} is {count}")