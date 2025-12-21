year = int(input("enter year: "))

if((year % 400 == 0) or (year % 4 == 0) and (year != 0)):
   print("is is a leap year")
else:
   print("it is not leap year")   