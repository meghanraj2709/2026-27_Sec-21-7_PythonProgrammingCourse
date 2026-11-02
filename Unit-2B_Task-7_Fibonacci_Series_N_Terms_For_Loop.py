#To print fibonacci series up to N terms
n = int(input("Enter the N term: "))
a = 0
b = 1
for i in range (n):
    print(a)
    next = a + b
    a = b
    b = next