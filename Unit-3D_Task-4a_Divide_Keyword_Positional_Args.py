#program that defines a function divide
def divide(num1,num2):
    divide = num1/num2
    return divide
result_1 = divide(num2 = 100,num1 = 4)
print("The result of dividing 100 by 4 with keyword arguments =",result_1)
result_2 = divide(100,4)
print("The result of dividing 100 by 4 with positional arguments =",result_2)