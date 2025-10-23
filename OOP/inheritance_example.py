class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def details(self):
        print(f"Name:{self.name}\nGrade:{self.grade}")

student1=Student("Aparna","A")
student2=Student("Anusha","A+")
student1.details()
student2.details()