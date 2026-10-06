#program to print the grade of a student using an elif ladder 
marks = int(input("Enter the marks of the student:"))
if marks >= 90:
    print("The grade of the student is A (marks =",marks,")")
elif marks >= 80 and marks < 90:
    print("The grade of the student is B (marks =",marks,")")
elif marks >= 70 and marks < 80:
    print("The grade of the student is C (marks =",marks,")")
else:
    print("The grade of the student is D (marks =",marks,")")