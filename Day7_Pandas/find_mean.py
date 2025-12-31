import pandas as pd

df = pd.read_csv("big_employee_data.csv")
print("Average Salary:", df['Salary'].mean())