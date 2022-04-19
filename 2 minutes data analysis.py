import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv("car-sales-extended.csv")
df

a=ProfileReport(df)
a.to_file(output_file=("C:\\Users\\acer\\Desktop\\car_extended_report.pdf"))