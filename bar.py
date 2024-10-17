import plotly.express as px
import pandas as pd

df=pd.read_csv("sample.csv")
print(df.head())

h=px.bar(df,x="FirstName",y="Score",color="FirstName")
h.show()
