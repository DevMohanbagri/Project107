import pandas as pd 
import csv
import plotly.express as px

df = pd.read_csv('students.csv')

#student_df = df.loc[df['student_id']=='TRL_987']
mean =(df.groupby(['student_id','level'])['attempt'].mean())
print(mean)

fig = px.scatter(
    mean,
    x = df['student_id'],
    y = df['level'],
    size = df['attempt'],
    color = df['attempt']

)

fig.show()