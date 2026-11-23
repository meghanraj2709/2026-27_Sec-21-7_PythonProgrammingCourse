#program that shows a local variable inside a function does not change a global variable with the same name
x = 10
def demo():
    x = 20  # local assignment
    print("Inside function, x =", x)
demo()
print("Outside function, x =", x)