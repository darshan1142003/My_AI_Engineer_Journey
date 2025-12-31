import pandas as pd

df = pd.read_csv("big_employee_data.csv")
rows, column = df.shape
print("number of rows:", rows)
print("number of columns:", column)
