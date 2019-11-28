
import pandas as pd
import os

os.chdir('/Users/change521/Desktop/Solar-Electric')

df = pd.read_csv('Solar_Electric_Programs.csv')

project_number = df.iloc[:,2]
city = df.iloc[:,3]
county = df.iloc[:,4]
state = df.iloc[:,5]
zip_code = df.iloc[:,6]
location_1 = df.iloc[:,30]


df2 = pd.concat([project_number, city, county, state, zip_code, location_1], axis = 1)

df2.to_csv('Solar_Electric_Loaction.csv')
