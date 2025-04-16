 #**FizzBuzz**: Write a program that prints numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number, and
# for multiples of 5, print "Buzz". For numbers that are multiples of both, print "FizzBuzz".
i = 1
while i <= 100:
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1  # Correctly indented