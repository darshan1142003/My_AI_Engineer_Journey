import pandas as pd

df = pd.read_csv("big_employee_data.csv")
filtered = df[df["Salary"] > 145000]
print(filtered)