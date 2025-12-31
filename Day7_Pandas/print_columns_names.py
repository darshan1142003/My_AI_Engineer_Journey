import pandas as pd

df = pd.read_csv("big_employee_data.csv")
for i in df.columns:
    print(i)