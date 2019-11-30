import pandas as pd
import matplotlib.pyplot as plt

def draw_his(df, col, percent, df_name ,figsize=(14,8)):
    plt.clf()
    thresh = sorted(df[col].tolist())[int(percent* len(df))]
    sub_df = df[df[col] < thresh]
    sub_df.hist(col, bins=10, figsize=figsize)
    plt.savefig(df_name + "_" + col + "Hist.png")

def draw_bar(df, col, df_name,figsize=(14,8)):
    plt.clf()
    df.groupby(col)[col].agg(["count"]).plot(kind='bar', figsize=figsize, title="{} count".format(col))
    plt.savefig(df_name + "_" + col + "Count.png")

# Solar_Electric_Loaction.csv
df = pd.read_csv("Solar_Electric_Loaction.csv")
print(df.columns)
draw_bar(df,"County","Solar_Electric_Loaction")


#Solar_Electric_Project_Status
df = pd.read_csv("Solar_Electric_Project_Production.csv")
print(df.columns)
draw_his(df, "$Incentive", 0.98,"Solar_Electric_Project_Production" )
draw_his(df, "Total Nameplate kW DC", 0.98,"Solar_Electric_Project_Production" )
draw_his(df, "Expected KWh Annual Production", 0.98,"Solar_Electric_Project_Production" )
draw_his(df, "$Incentive", 0.98,"Solar_Electric_Project_Production" )

#Solar_Electric_Project_Status
df = pd.read_csv("Solar_Electric_Project_Status.csv")
print(df.columns)
draw_bar(df, "Project Status","Solar_Electric_Project_Status")
draw_his(df, "Project Cost",0.98, "Solar_Electric_Project_Status")

#Solar_Electric_Project_Type
df = pd.read_csv("Solar_Electric_Project_Type.csv")
print(df.columns)
draw_bar(df, "Purchase Type","Solar_Electric_Project_Type")
draw_bar(df, "Remote Net Metering","Solar_Electric_Project_Type")
draw_bar(df, "Affordable Solar","Solar_Electric_Project_Type")
draw_bar(df, "Community Distributed Generation","Solar_Electric_Project_Type")

#Solar_Electric_ProjectID
df = pd.read_csv("Solar_Electric_ProjectID.csv")
print(df.columns)
df["Date Application Received Year"] = df["Date Application Received"].apply(lambda x : x.split("/")[-1] if isinstance(x, str) else "NULL")
df["Date Completed Year"] = df["Date Completed"].apply(lambda x : x.split("/")[-1] if isinstance(x, str) else "Not Completed")
draw_bar(df, "Program Type","Solar_Electric_ProjectID")
draw_bar(df, "Date Application Received Year", "Solar_Electric_ProjectID")
draw_bar(df, "Date Completed Year", "Solar_Electric_ProjectID")

#Solar_Electric_ProjectProvider
df = pd.read_csv("Solar_Electric_ProjectProvider.csv")
print(df.columns)
draw_bar(df, "Primary Inverter Manufacturer","Solar_Electric_ProjectProvider",figsize=(40,8))
draw_bar(df,"Primary PV Module Manufacturer","Solar_Electric_ProjectProvider",figsize=(60,8))

#Solar_Electric_PV_Model
df = pd.read_csv("Solar_Electric_PV_Model.csv")
print(df.columns)
draw_bar(df,"Primary PV Module Manufacturer", "Solar_Electric_PV_Model", figsize=(60,8))
draw_his(df, "Total PV Module Quantity", 0.98, "Solar_Electric_PV_Model")