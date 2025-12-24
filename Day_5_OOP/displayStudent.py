class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def Display(self):
        print("Name:",self.name)    
        print("Marks:",self.marks)
        print("")

s1=Student("Darshan", 85)            
s2=Student("Mansi", 95)            
s3=Student("Parth", 25)

s1.Display()
s2.Display()
s3.Display()