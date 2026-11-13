#program that defines a function using *args to find the sum of any number of values
# Example solution: sum using *args
def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total

print(sum_values(1, 2, 3))
print(sum_values(10, 20, 30, 40))