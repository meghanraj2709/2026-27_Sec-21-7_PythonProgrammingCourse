# to remove duplicate elements from a list
list_data = [3, 7, 13, 6, 7, 46, 3]
unique = []
for item in list_data:
    if item not in unique:
        unique.append(item)
print("Original:", list_data)
print("Without duplicates:", unique)