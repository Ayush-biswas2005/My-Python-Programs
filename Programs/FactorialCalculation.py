#**Factorial Calculation**: Implement a function using recursion to find the factorial of a given number.
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return fact (n-1) * n
print(fact(6))