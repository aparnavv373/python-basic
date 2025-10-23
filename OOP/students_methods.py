class Student:
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def greet(self):
        print(f"Hello,my name is {self.name}, I am {self.age} years old.")
    
student1=Student("Aparna",22)
student2=Student("Anusha",24)
student1.greet()
student2.greet()