#program that uses a global counter and increments it inside a function using the global keyword
counter = 0
def increment():
    global counter
    counter = counter + 1
    print("Inside function, counter =", counter)
print("Before:", counter)
increment()
print("After:", counter)