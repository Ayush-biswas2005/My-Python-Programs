#**Reverse a String**: Without using built-in reverse functions, write a program that reverses a string.
a=input("Enter the string:")
reversed_string = ""
for char in a:
    reversed_string = char+reversed_string
print("The answer is:", reversed_string)