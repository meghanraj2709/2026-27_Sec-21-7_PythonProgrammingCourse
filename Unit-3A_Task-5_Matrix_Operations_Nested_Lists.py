# to perform matrix operations using nested lists
matrix_a = [[12, 3], [24, 7]]
matrix_b = [[35, 34], [1, 2]]
rows = len(matrix_a)
cols = len(matrix_a[0])
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)
print("Matrix A:", matrix_a)
print("Matrix B:", matrix_b)
print("Sum:", result)