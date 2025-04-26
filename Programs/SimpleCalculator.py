#** Simple Calculator ** – Write a program that takes two numbers and an operation(+, -, *, /) and returns the result.
a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
operation= input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
else:
    result = "Invalid operation"
print("Result:", result)