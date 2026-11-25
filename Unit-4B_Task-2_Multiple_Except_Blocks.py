#reads a list index and handles ValueError and IndexError separately
list_data = [7, 77, 777]
try:
    index = int(input("Enter index: "))
    value = list_data[index]
    print("Value:", value)
except ValueError:
    print("Please enter a valid integer index.")
except IndexError:
    print("Index is out of range.")