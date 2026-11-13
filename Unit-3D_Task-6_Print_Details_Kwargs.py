#program that defines a function **kwargs to print each key and value from kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_details(name="Meghan", age=18, city="Vijayawada")