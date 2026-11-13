#program that defines a function to convert temperature from Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print("Required temperature in fahrenheit =",fahrenheit)