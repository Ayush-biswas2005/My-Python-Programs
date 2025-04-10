a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
if (a>=b and a>=c):
    print("First number is largest",a)
elif (b>=c):
    print("Second number is largest",b)
else:
    print("Third number is largest",c)
