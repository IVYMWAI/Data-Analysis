#Importing the dataset and libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("cab_rides.csv")
print(df)

#getting general information about the cab_rides dataset
list(df.columns.values)

#Checking for missing values
df.isnull().sum()
#There are no null values

#Dropping any duplicate values
df.drop_duplicates(inplace=True)


#Finding the correlation betweeen distance and price for both uber and lyft


##DATA ANALYSIS and visualization
#seperate the cab dataset into lyft and uber
df["cab_type"].value_counts()
uber_df=df[df["cab_type"] == "Uber"]
lyft_df=df[df["cab_type"] =="Lyft"] 

#Comparing Uber and Lyft
y=[df.cab_type[(df.cab_type) == "Uber"].count(),\
 df.cab_type[df.cab_type =="Lyft"].count()]

cab_type=["Uber","Lyft"]
plt.pie(y, labels=cab_type, startangle=90, autopct='%.1f%%')
plt.show()

























































