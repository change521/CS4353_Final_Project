
import pandas as pd
import os

os.chdir('/Users/change521/Desktop/Solar-Electric')

df = pd.read_csv('Solar_Electric_Programs.csv')

project_number = df.iloc[:,1]
incentive = df.iloc[:,22]
total_nameplate_KW_DC = df.iloc[:,23]
excepted_KWh_annual_production = df.iloc[:,24]



df2 = pd.concat([project_number, incentive, total_nameplate_KW_DC, excepted_KWh_annual_production], axis = 1)

df2.to_csv('Solar_Electric_Project_Production.csv')
