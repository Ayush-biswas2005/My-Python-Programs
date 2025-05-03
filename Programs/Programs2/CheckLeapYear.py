# Write a program that determines whether a given year is a leap year or not.
a=int(input("Enter a year:"))
if(a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(a, "is a leap year.")
else:
    print(a, "is not a leap year.")