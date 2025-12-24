class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

s1 = Student("Darshan", 85)
print(f"name of the student is {s1.name} and marks is {s1.marks}")
s2 = Student("Mansi", 95)
print(f"name of the student is {s2.name} and marks is {s2.marks}")
s3 = Student("Parth", 25)
print(f"name of the student is {s3.name} and marks is {s3.marks}")
