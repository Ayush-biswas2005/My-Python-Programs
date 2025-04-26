# **Prime Number Check**: Write a program to check if a number is prime.
# Input from user
a=int(input("Enter a number:"))
if a < 2:
    print(f"{a} is not a prime number")
else:
    is_prime = True
    for i in range(2, a):
        if a%i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{a} is a prime number")
    else:
        print(f"{a} is not a prime number")