import pandas as pd
import os

os.chdir('/Users/change521/Desktop/Solar-Electric')

df = pd.read_csv('Solar_Electric_Programs.csv')

project_number = df.iloc[:,1]
program_type = df.iloc[:,7]
date_application_received = df.iloc[:,11]
data_completed = df.iloc[:,12]



df2 = pd.concat([project_number, program_type, date_application_received, data_completed], axis = 1)

df2.to_csv('Solar_Electric_ProjectID.csv')
