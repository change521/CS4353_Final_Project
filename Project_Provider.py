
import pandas as pd
import os

os.chdir('/Users/change521/Desktop/Solar-Electric')

df = pd.read_csv('Solar_Electric_Programs.csv')

project_number = df.iloc[:,1]
contractor = df.iloc[:,14]
primary_inverter_manufacturer = df.iloc[:,15]
primary_PV_module_manufacturer = df.iloc[:,18]



df2 = pd.concat([project_number, contractor, primary_inverter_manufacturer, primary_PV_module_manufacturer], axis = 1)

df2.to_csv('Solar_Electric_ProjectProvider.csv')
