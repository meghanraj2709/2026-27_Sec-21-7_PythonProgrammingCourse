#To check a palindrome number
num = int(input("Enter a number: "))
originalnum = num
work = num
rev = 0
while work > 0:
    digit = work % 10
    rev = rev * 10 + digit
    work = work // 10
if rev == originalnum:
    print(f"{originalnum} is a palindrome.")
else:
    print(f"{originalnum} is not a plaindrome.")