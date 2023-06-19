# Refactor calculator using OOP

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Cannot divide by zero"

    def mod(self, x, y):
        return x % y


# Creating an instance of the Calculator class
calculator = Calculator()

# Adding user input
equation = input("Type in a basic equation: \n")

equation_array = equation.split(" ")


if equation_array[1] == '+':
    print(calculator.add(int(equation_array[0]), int(equation_array[2])))
elif equation_array[1] == '-':
    print(calculator.subtract(int(equation_array[0]), int(equation_array[2])))
elif equation_array[1] == '/':
    print(calculator.divide(int(equation_array[0]), int(equation_array[2])))
elif equation_array[1] == '*':
    print(calculator.multiply(int(equation_array[0]), int(equation_array[2])))
elif equation_array[1] == '%':
    print(calculator.mod(int(equation_array[0]), int(equation_array[2])))
else:
    print("That is not an equation...")


