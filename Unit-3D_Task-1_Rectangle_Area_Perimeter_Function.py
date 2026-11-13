# program that defines a function to calculate the area and perimeter of a rectangle 
def area_perimeter_of_rectangle(length,breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area,perimeter
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area,perimeter = area_perimeter_of_rectangle(length,breadth)
print("Area of the rectangle =",area)
print("Perimeter of the rectangle =",perimeter)