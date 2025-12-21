marks = int(input("enter your marks: "))

if(marks >= 90):
    print("your grade is A")
elif((marks >= 75) and (marks < 90)):
    print("your grade is B")
elif((marks >= 50) and (marks < 75)):
    print("your grade is C")
elif((marks >= 35) and (marks < 50)):
    print("your grade is D")
elif(marks < 35):
    print("you are failed")    