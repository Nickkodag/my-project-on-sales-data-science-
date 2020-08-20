import pandas as pd
import os
import matplotlib.pyplot as plt
from intercool import Combination
from collections import Counter 
df =pd.read_csv("./Sales_Data/Sales_April_2019.csv")

files=[file for file in os.listdir('./Sales_Data')]
all_month_data=pd.DataFrame()
for file in files:
     pd.read_csv("./Sales_Data/"+file)
     all_month_data=pd.concat([all_month_data,df])
#print(all_month_data.head())  
all_month_data.to_csv("all_data_csv",index=False)   
alldata=pd.read_csv('all_data_csv')
#print(alldata.head())
#best month of sales
#clean data
nandf=alldata[alldata.isna().any(axis=1)]
print(nandf.head())
alldata=alldata.dropna(how="all")
print(alldata.head(100))
#or Fuction
tempdf=alldata[alldata['Data'].str[0:2]!="or"]
#CONVERT COLUMN TO INT

alldata['Quantity Ordered']= pd.to_numeric(alldata['Quantity Ordered'])#make int
alldata["Price  Each"]=pd.to_numeric(alldata["Price  Each"]) #make float
print(tempdf.head())
#adding month coloum
alldata['Order Date ']=pd.to_datetime['Order Date']
alldata['Month']=alldata['Data'].str[0:2]
alldata['month']=alldata['month'].astype('int32')
print(alldata.head())
#add sales coloum
alldata['sales']=alldata['Quantity Ordered']*alldata['Price Each']
#ADD CITY COLUMN
#using.apply mothod
def get_city(address):
     return address.split(',')[1]
def get_state(address):
     return address.split(',')[2].split('')
     
     
alldata['City']=alldata['Purchase Address'].apply(lambda x: f'{get_city(x)} ({get_state(x)})')
#group by month and sum
result=alldata.groupby('month').sum()

print(result)
#BEST MONTH FOR SALE     
months=range (1,13)
plt.bar(months,result['sales'])
plt.xtricks()
plt.xlabel("sales in usd$")
plt.ylabel("month number")
plt.show()
#city with high numnber of sales
result=alldata.groupby('City').sum()
print(result)

cities=[City for city,df in alldata.groupby('City')]
plt.bar(months,result['sales'])
plt.xtricks(cities,rotation="vertical",size=8)
plt.xlabel("sales in usd$")
plt.ylabel("cities")
plt.show()
#what time we can show ad ton maximas sales
alldata['Order Date ']=pd.to_datetime['Order Date']
alldata['Hour']=datetime['Order Date'].dt.hour
alldata['Minute']=datetime['Order Date'].dt.minute
print(alldata(head())

plt.plot(hours, alldata.groupby(['Hour']).count())
print (alldata.groupby('Hour')].count()))
plt.xticks(hour)
plt.grid()
plt.show()
#what product are most often sold together
df=alldata.alldata['Order ID'].duplicated(keep=False)
df['Group']=df.groupby('Order,ID').tranform(lamdax:','.join(x))
df=df[["order ID","Group"]],drep_duplicates()
print(df(head))
count=counter()
for row in df ['Group"]:
     row_list = row.split(",")
     count.update(Counter(combination(row_list,2)))
for key ,value in count.most_commom(10):
     print(key,value)
#what product sold most

print(alldata(head))
quantity_order=product_group.sum()['Quantity Order ']     
products=[product for product,df in product_group]
plt.bar(products,quantity_Order)
plt.show()
price=alldata.groupby('Product').mean()['Price Each']
print(price)
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products, Quantity Order, 'g-')
ax2.plot(products, price, 'b-')

ax1.set_xlabel('products name')
ax1.set_ylabel('Quantity Order', color='g')
ax2.set_ylabel(' price ', color='b')

plt.show()