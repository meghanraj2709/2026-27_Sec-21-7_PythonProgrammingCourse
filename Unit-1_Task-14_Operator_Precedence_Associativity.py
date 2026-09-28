#operator precedence and associativity
a, b, c = 2, 3, 4
result = a + (b * c)   
print(result)          
print(a + b * c)

a, b, c = 10, 3, 2
left_to_right = (a - b) - c
print(left_to_right)  
print(a - b - c)       

a, b, c = 2, 3, 2
right_to_left = a ** (b ** c)
print(right_to_left)
print(a ** b ** c)