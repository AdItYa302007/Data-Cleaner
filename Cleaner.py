import pandas as pd 
import csv

df= pd.read_csv("final.csv")
print(df.shape)

del df["Star_name"]
del df["Mass"]
del df["Radius"]
del df["Distance"]
del df["Luminosity"]

print(df.shape)


df.to_csv('cleanedfinal.csv')