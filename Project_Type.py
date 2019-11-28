
import pandas as pd
import os

os.chdir('/Users/change521/Desktop/Solar-Electric')

df = pd.read_csv('Solar_Electric_Programs.csv')

project_number = df.iloc[:,1]
purchase_type = df.iloc[:,10]
remote_net_metering = df.iloc[:,25]
affordable_solar = df.iloc[:,26]
community_distributed_generation = df.iloc[:,27]



df2 = pd.concat([project_number, purchase_type, remote_net_metering, affordable_solar,community_distributed_generation], axis = 1)

df2.to_csv('Solar_Electric_Project_Type.csv')
