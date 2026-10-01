# Task 3: Simple Class and Inheritance
# Define a person class with attributes name and age, 
# and a method greet() that prints a greeting message. 
# Then, define a Student class that inherits from Person 
# and adds an additional attribute student_id. 
# Create an instance of Student and call the greet() method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student = Student("Viktoria", 25, "S12345")
student.greet()
print(student.student_id)