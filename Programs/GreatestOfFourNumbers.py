#Write a Python program to find the greatest of four numbers entered by the user.
a=int(input("Einter the first number;"))
b=int(input("Einter the second number;"))
c=int(input("Einter the third number;"))
d=int(input("Einter the fourth number;"))
if(a>=b and a>=c):
    print("First numbert is largest",a)
elif(b>=a and b>=c):
    print("Second numbert is largest",b)
elif(c>=a and c>=b):
    print("Third numbert is largest",c)
else:
    print("Fourth numbert is largest",d)