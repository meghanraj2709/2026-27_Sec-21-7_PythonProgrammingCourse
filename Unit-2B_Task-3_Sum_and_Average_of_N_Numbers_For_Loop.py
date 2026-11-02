#To find the sum and average of N numbers using for loop
total_numbers = int(input("Enter how many numbers: "))
total_sum = 0
for input_index in range(total_numbers):
    entered_number = float(input("Enter a number: "))
    total_sum = total_sum + entered_number
average = total_sum/total_numbers
print("Sum =",total_sum)
print("Average",average)