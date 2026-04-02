#Create a class with __init__ and __str__ to display object details.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

s = Student("Ayush", 20)
print(s)