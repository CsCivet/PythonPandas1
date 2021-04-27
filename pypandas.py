import pandas as pd
import csv
import os

# read from the data
df = pd.read_csv('Train.csv')

# sort the data
df.sort_values(["Warehouse_block", "Mode_of_Shipment"], axis=0,ascending=True, inplace=True)

# applying search conditions
sc1 = pd.DataFrame(df, columns= ['Warehouse_block','Customer_care_calls','Customer_rating','Reached.on.Time_Y.N'])
sc2 = pd.DataFrame(df, columns= ['Mode_of_Shipment','Reached.on.Time_Y.N'])
sc3 = pd.DataFrame(df, columns= ['Customer_rating','Discount_offered'])

# pivot
pivot1 = df.pivot_table(index=['Product_importance'], aggfunc='size')
pivot2 = df.pivot_table(index=['Reached.on.Time_Y.N'], aggfunc='size')
pivot3 = df.pivot_table(index=['Gender'], aggfunc='size')


# calculate the total
total = df['Weight_in_gms'].sum()
#Calculate the total where raw value = X ( using Boolean indexing )
#in this case where column 'Mode_of_Shipment' is equal to "Flight" and then sum the corresponding rows of column 'Weight_in_gms'.
total2=df.loc[df['Mode_of_Shipment'] == "Flight", 'Weight_in_gms'].sum()

print(total)
print(total2)

#creating csv
df.to_csv('df.csv')

sc1.to_csv('sc1.csv')
sc2.to_csv('sc2.csv')
sc3.to_csv('sc3.csv')

pivot1.to_csv('pivot1.csv')
pivot2.to_csv('pivot2.csv')
pivot3.to_csv('pivot3.csv')

dfhtml = pd.read_csv('df.csv')
sc1html = pd.read_csv('sc1.csv')
sc2html = pd.read_csv('sc2.csv')
sc3html = pd.read_csv('sc3.csv')

# creating html
dfhtml.to_html('mydata.html')
sc1html.to_html('sc1html.html')
sc3html.to_html('sc2html.html')
sc3html.to_html('sc3html.html')

# removing the csv files
os.remove ('df.csv')
os.remove ('sc1.csv')
os.remove ('sc2.csv')
os.remove ('sc3.csv')
