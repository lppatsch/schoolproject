import random
class Student:
 def __init__(self, name, age):
 self.name = name
 self.age = age
 def get_info(self):
 print("Name: " + self.name)
 print("Age: " + str(self.age))
s1 = Student("John", 25)
s2 = Student("Amy", 30)
s1.get_info()
s2.get_info()