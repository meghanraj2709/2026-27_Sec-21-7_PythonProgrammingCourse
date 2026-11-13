# program that defines a function taking marks of three subjects as parameters and returns the total and average
def total_average_of_three_subjects(a,b,c):
    total = a + b + c
    average = total/3
    return total,average
a = int(input("Enter the marks of first subject: "))
b = int(input("Enter the marks of second subject: "))
c = int(input("Enter the marks of third subject: "))
total,average = total_average_of_three_subjects(a,b,c)
print("Total marks of three subjects =",total)
print("The average marks of the three subjects = ",average)