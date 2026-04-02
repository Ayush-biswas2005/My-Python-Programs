# class Student:
#     # name="Ayush"
#     college_name="UEMK"
#     def __init__(self, name,marks):
#         self.name=name
#         self.marks=marks
#         # print("adding new student in Database..")

#     def welcome(self):
#         print("Welcome",self.name)

#     def get_marks(self):
#         return self.marks
    
# s1=Student("Ayush",99)
# # print(s1.name,s1.marks)

# # s2=Student("Riju",87)
# # print(s2.name,s2.marks)
# s1.welcome()
# print(s1.get_marks())

# # print(Student.college_name)


# # class Car:
# #     color="blue"
# #     name="BMW"

# # c1=Car()
# # print(c1.color)
# # print(c1.name)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(self.name,"Your Avg score is:",sum/3)
s1=Student("Ayush",{90,98,99})
s1.get_avg()