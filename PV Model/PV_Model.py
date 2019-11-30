
import pandas as pd
import os

os.chdir('/Users/change521/Desktop/Solar-Electric')

df = pd.read_csv('Solar_Electric_Programs.csv')

project_number = df.iloc[:,1]
PV_module_model_number = df.iloc[:,19]
primary_PV_module_manufacturer = df.iloc[:,18]
total_PV_module_quantity = df.iloc[:,20]



df2 = pd.concat([project_number, PV_module_model_number, primary_PV_module_manufacturer, total_PV_module_quantity], axis = 1)

df2.to_csv('Solar_Electric_PV_Model.csv')
