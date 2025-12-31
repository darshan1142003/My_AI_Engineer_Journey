import pandas as pd

df = pd.read_csv("big_employee_data.csv")
sort = df.sort_values(by="Salary")
print(sort)