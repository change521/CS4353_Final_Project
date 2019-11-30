
import pandas as pd
import os

os.chdir('/Users/change521/Desktop/Solar-Electric')

df = pd.read_csv('Solar_Electric_Programs.csv')

project_number = df.iloc[:,1]
project_status = df.iloc[:,13]
contractor = df.iloc[:,14]
project_cost = df.iloc[:,21]



df2 = pd.concat([project_number, project_status, contractor, project_cost], axis = 1)

df2.to_csv('Solar_Electric_Project_Status.csv')
