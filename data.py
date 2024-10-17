import plotly.express as px
import pandas as pd

# print(px.data.gapminder())
data=px.data.gapminder().query("country=='Canada'")

# print(data.head())

b=px.bar(data, x="year",y="pop",color="pop")
b.show()